from pydantic import BaseModel, Field

class BarModel(BaseModel):
    whatever: tuple[int, ...]

class FooBarModel(BaseModel):
    banana: float | None = 1.1
    foo: str = Field(serialization_alias='foo_alias')
    bar: BarModel

m = FooBarModel(banana=3.14, foo='hello', bar={'whatever': (1, 2)})

# returns a dictionary:
print(m.model_dump()) # mode's default is 'python'
#> {'banana': 3.14, 'foo': 'hello', 'bar': {'whatever': (1, 2)}}

print(m.model_dump(by_alias=True))
#> {'banana': 3.14, 'foo_alias': 'hello', 'bar': {'whatever': (1, 2)}}

print('-------------------------- JSON --------------------------------')
print(m.model_dump(mode='json'))
print(m.model_dump_json())

print(m.model_dump(mode='json', by_alias=True))
#> {'banana': 3.14, 'foo_alias': 'hello', 'bar': {'whatever': [1, 2]}}