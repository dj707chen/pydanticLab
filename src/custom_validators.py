# /Users/weiping/repoMy/pydantic/docs/examples/custom_validators.md

import datetime as dt
from dataclasses import dataclass
from pprint import pprint
from typing import Annotated, Any

import pytz
from pydantic_core import CoreSchema, core_schema

from pydantic import (
    GetCoreSchemaHandler,
    PydanticUserError,
    TypeAdapter,
    ValidationError,
    ValidatorFunctionWrapHandler,
)


@dataclass(frozen=True)
class MyDatetimeValidator:
    tz_constraint: str | None = None

    def tz_constraint_validator(
        self,
        value: dt.datetime,
        handler: ValidatorFunctionWrapHandler,  # (1)!
    ):
        """Validate tz_constraint and tz_info."""
        # handle naive datetimes
        print(f"[MyDatetimeValidator.tz_constraint_validator] tz_constraint={self.tz_constraint}")
        if self.tz_constraint is None:
            assert (
                value.tzinfo is None
            ), 'tz_constraint is None, but provided value is tz-aware.'
            return handler(value)

        # validate tz_constraint and tz-aware tzinfo
        if self.tz_constraint not in pytz.all_timezones:
            raise PydanticUserError(
                f'Invalid tz_constraint: {self.tz_constraint}',
                code='unevaluable-type-annotation',
            )
        result = handler(value)  # (2)!
        assert self.tz_constraint == str(
            result.tzinfo
        ), f'Invalid tzinfo: {str(result.tzinfo)}, expected: {self.tz_constraint}'

        return result

    def __get_pydantic_core_schema__(
        self,
        source_type: Any,
        handler: GetCoreSchemaHandler,
    ) -> CoreSchema:
        return core_schema.no_info_wrap_validator_function(
            self.tz_constraint_validator,
            handler(source_type),
        )


LA = 'America/Los_Angeles'
dt_validator_ta = TypeAdapter(Annotated[dt.datetime, MyDatetimeValidator(LA)])
print(
    dt_validator_ta.validate_python(dt.datetime(2023, 1, 1, 0, 0, tzinfo=pytz.timezone(LA)))
)
#> 2023-01-01 00:00:00-07:53
