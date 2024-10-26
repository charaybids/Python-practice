'''
quadratic equation is represented as ax**2 + bx + c = 0. The general formula to find its roots (x-values for which y = 0) is:

example

This formula provides two roots: x1, x2. The value inside the square root, b2-4ac is known as the discriminant (D). 
Based on the value of the discriminant, a quadratic equation can have:

two distinct real roots (D > 0);
one real root (D = 0);
no real roots (D < 0).
Your code must return Iterable containing two values: the roots x1, x2, sorted descending. 
If there's only one real root, both values will be the same. 
If there are no real roots, the Iterable should contain the string "No real roots".
'''

from collections.abc import Iterable
from typing import Union


def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[int | float] | str]:
    
    discriminant = b ** 2 - (4 * a * c)
    
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return sorted([x1, x2], reverse=True)
    
    elif discriminant == 0: 
        x = -b / (2 * a)
        return [x, x]
    
    else:
        return ['No real roots']
    
print("Example:")
print(list(quadratic_roots(1, 2, 3)))