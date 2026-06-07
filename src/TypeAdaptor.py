from typing_extensions import TypedDict

from pydantic import TypeAdapter, ValidationError


class User(TypedDict):
    name: str
    id: int

print("------------------------- validate_python ---------------------")
user_list_adapter: TypeAdapter[list[User]] = TypeAdapter(list[User])
user_list:                     list[User]  = user_list_adapter.validate_python([{'name': 'Fred', 'id': '3'}])
print(repr(user_list))
#> [{'name': 'Fred', 'id': 3}]

try:
    user_list_adapter.validate_python(
        [{'name': 'Fred', 'id': 'wrong', 'other': 'no'}]
    )
except ValidationError as e:
    print(e)
    """
    1 validation error for list[User]
    0.id
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='wrong', input_type=str]
    """

print("------------------------- dump_json ---------------------")
print(repr(user_list_adapter.dump_json(user_list)))
#> b'[{"name":"Fred","id":3}]'

print("--------------------- Parsing data into a specified type ----------------")
from pydantic import BaseModel, TypeAdapter

class Item(BaseModel):
    id: int
    name: str

# `item_data` could come from an API call, eg., via something like:
# item_data = requests.get('https://my-api.com/items').json()
item_data: list[dict] = [{'id': 1, 'name': 'My Item'}] # Type annotation not enforced here
print(f"type of item_data={type(item_data)}")
print(f"type of item_data[0]={type(item_data[0])}")

items = TypeAdapter(list[Item]).validate_python(item_data) # Type annotation enforced here
print(items)
#> [Item(id=1, name='My Item')]

print("--------------- Rebuilding a TypeAdapter's schema --------------")
from pydantic import ConfigDict, TypeAdapter

ta = TypeAdapter('MyInt', config=ConfigDict(defer_build=True))
# some time later, the forward reference is defined
MyInt = int

ta.rebuild()
assert ta.validate_python(1) == 1

# Call rebuild() again won't wipe out the already built schema,
# comment out this line will result error.
ta = TypeAdapter('MyInt', config=ConfigDict(defer_build=True))

# some time later, the forward reference is defined
MyInt = str

ta.rebuild()
assert ta.validate_python("1") == "1"
