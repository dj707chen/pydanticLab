from typing import ClassVar
from pprint import pformat, pprint

# Without Pydantic, the best is to use pprint

class Starship:
    stats: ClassVar[dict[str, int]] = {} # class variable
    damage: int = 10                     # instance variable

ss1 = Starship()
ss1.damage = 11
ss2 = Starship()
ss2.damage = 12
print(f"ss1={pformat(ss1)}")
pprint(ss1)
print(f"ss1.stats={ss1.stats}")

# By default, the semantics of ClassVar is not enforced,
# so you can set Class variable stats on instance variable!
ss2.stats = {"len": 200}

print(f"ss2={pformat(ss2)}")
pprint(ss2)
print(f"ss2.stats={ss2.stats}")
print(f"ss1.stats={ss1.stats}")

print("------------------------------------------------------------------------------")
print("Set class variables via class name:")
# ss1.stats = {"len": 100} # if this line is un-commented out, then the next line has not effect
Starship.stats = {"len": 300}
print(f"ss1.stats={ss1.stats}") # ss1.stats={'len': 100}
print(f"ss2.stats={ss2.stats}") # ss1.stats={'len': 100}
Starship.damage = 12 # no effect, since this field is not class variable
print(f"ss1.damage={ss1.damage}") # ss1.damage=11

print("------------------------------------------------------------------------------")
# Without Pydantic, the best is to use pprint
d = {"name": "Wei", "age": 61, "Weight": 138, "experiences": ["Java", "Scala", "Rust"]}
print(d)
pprint(d)
