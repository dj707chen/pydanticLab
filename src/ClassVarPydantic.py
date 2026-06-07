from typing import ClassVar

from pydantic import BaseModel

class Starship(BaseModel):
    stats: ClassVar[dict[str, int]] = {} # class variable
    damage: int = 10                     # instance variable

ss1 = Starship(damage=11)
ss2 = Starship(damage=12)
print(f"ss1={ss1.model_dump()}")
print(f"ss1.stats={ss1.stats}")

# By default, the semantics of ClassVar is not enforced, but Pydantic models do!
# so you can's set Class variable stats on Pydantic instance variable!
# ss2.stats = {"len": 100}
# If you try, you'll get error:
#     AttributeError: 'stats' is a ClassVar of `Starship` and cannot be set on an instance.
#     If you want to set a value on the class, use `Starship.stats = value`.

Starship.stats = {"len": 100}
print(f"ss2={ss2.model_dump()}")
print(f"ss2.stats={ss2.stats}")
