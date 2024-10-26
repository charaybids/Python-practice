'''
Given a string, return all possible permutations of its characters, sorted alphabetically.
'''

from collections.abc import Iterable    
from itertools import permutations

def string_permutations(s: str) -> Iterable[str]:
    str_perm = []
    for p in permutations(s):
        str_perm.append(''.join(p))
        
    return sorted(str_perm)


print("Example:")
print(list(string_permutations("ab")))