# https://github.com/dj707chen/pydantic/blob/a20c0ee267150c3bb0f82bf05e0806fa65b1e70c/docs/index.md#L56-L89

from datetime import datetime
from typing import Any
from pydantic import BaseModel, PositiveInt
from pprint import pprint

class User(BaseModel):
    id: int  # (1)!
    name: str = 'John Doe'  # (2)!
    signup_ts: datetime | None  # (3)!
    tastes: dict[str, PositiveInt]  # (4)!
    def check_taste(self, **kwargs: PositiveInt) -> None:
        for k, v in kwargs.items():
            if v <= 0:
                raise ValueError(f'Taste {k} should be greater than 0, but got {v}')
            print(f'Taste {k} is {v}')

external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',  # (5)!
    'tastes': {
        'wine': 9,
        b'cheese': 7,  # (6)!
        'cabbage': '1',  # (7)!
    },
}
user1 = User(**external_data)
user2 = User(
    id = 123,
    signup_ts = '2019-06-01 12:22',
    tastes = {
        'wine': 9,
        b'cheese': 7,
        'cabbage': '1'
    }
)
print(user1)
print(user2.id)  # (9)!
#> 123

assert user1 == user2
assert user1 is not user2

user1.check_taste(**user1.tastes)
"""
Taste wine is 9
Taste cheese is 7
Taste cabbage is 1
"""

user_dict: dict[str, Any] = user1.model_dump()
pprint(user_dict)
"""
{
    'id': 123,
    'name': 'John Doe',
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1},
}
"""
