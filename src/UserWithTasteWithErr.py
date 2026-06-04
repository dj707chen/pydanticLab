# https://github.com/dj707chen/pydantic/blob/a20c0ee267150c3bb0f82bf05e0806fa65b1e70c/docs/index.md#L56-L89

from datetime import datetime
from pprint import pprint
from pydantic import BaseModel, PositiveInt, ValidationError

class User(BaseModel):
    id: int  # (1)!
    name: str = 'John Doe'  # (2)!
    signup_ts: datetime | None  # (3)!
    tastes: dict[str, PositiveInt]  # (4)!

external_data_w_err = {
    # 'id': 123, # comment out this line intentionally to cause error
    'signup_ts': '2019-06-01 12:599',
    'tastes': {
        'wine': 9,
        b'cheese': 7,
        'cabbage': -1
    },
}

try:
    user = User(**external_data_w_err)
except ValidationError as e:
    pprint(e.errors())
    """
    [
    {'input': {'signup_ts': '2019-06-01 12:22',
                'tastes': {b'cheese': 7, 'cabbage': -1, 'wine': 9}},
    'loc': ('id',),
    'msg': 'Field required',
    'type': 'missing',
    'url': 'https://errors.pydantic.dev/2.13/v/missing'},
    {'ctx': {'gt': 0},
    'input': -1,
    'loc': ('tastes', 'cabbage'),
    'msg': 'Input should be greater than 0',
    'type': 'greater_than',
    'url': 'https://errors.pydantic.dev/2.13/v/greater_than'}
    ]
    """
