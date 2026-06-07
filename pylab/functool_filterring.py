
from itertools import filterfalse


l1 = list(1,2,3,4)
filterred = filterfalse(lambda x: x<3, l1)