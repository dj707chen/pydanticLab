from typing import Annotated

X = Annotated[int, "very", "important", "metadata"]
print(X)
#> typing.Annotated[int, 'very', 'important', 'metadata']
print(X.__metadata__)

x1: X = 1

# How can I get the annonation metadata from xx1 only through the instance reference x1 defined at line 8
# CC: it's not possible. At runtime, x1 is literally just the integer 1 — 
    # Python does not attach type annotation metadata to variable instances. 
    # Annotated[int, ...] is purely a static/type-checker construct; the metadata only exists on the type alias X,
    # not on any value assigned to a variable of that type.

    # You can confirm this:

    # >>> x1
    # 1
    # >>> type(x1)
    # <class 'int'>
    # >>> x1.__metadata__  # AttributeError: 'int' object has no attribute '__metadata__'
    # If you need metadata to travel with the value at runtime, you'd need a wrapper class that stores it explicitly —
    # Annotated alone doesn't do that.
