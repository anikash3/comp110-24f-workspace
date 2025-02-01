"""Create a funtion to visualize"""

__author__ = "730761368"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x: str =  "123"
y: str = "abc"

print(concat(str1 = x, str2 = y))
print(get_coords(xs=x, ys=y))
