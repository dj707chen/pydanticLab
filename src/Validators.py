# https://pydantic.dev/docs/validation/2.8/concepts/validators/#annotated-validators

from typing import Any, List, Annotated

from pydantic import BaseModel, ValidationError
from pydantic.functional_validators import BeforeValidator, AfterValidator

def before_validate(v: int) -> int:
    print(f'Before validation: {v}')
    return v

def check_squares(v: int) -> int:
    assert v**0.5 % 1 == 0, f'{v} is not a square number'
    return v

def double(v: Any) -> Any:
    return v * 2

MyNumber = Annotated[int,
                     BeforeValidator(lambda x: (x, print(f'Before validation in lambda: {x}'))[0]),
                     BeforeValidator(before_validate),
                     AfterValidator(double),
                     AfterValidator(check_squares),
                     ]

class DemoModel(BaseModel):
    number: List[MyNumber]

# print(DemoModel(number=[2, 8]))
#> number=[4, 16]

try:
    DemoModel(number=[2, 4])
except ValidationError as e:
    print(e)
    """
    1 validation error for DemoModel
    number.1
      Assertion failed, 8 is not a square number
    assert ((8 ** 0.5) % 1) == 0 [type=assertion_error, input_value=4, input_type=int]
    """