'''
In number theory, an Armstrong number (after Michael F. Armstrong) or narcissistic number in a given number base (10 for this mission) 
is a number that is the sum of its own digits each raised to the power of the number of digits. 
For example, 153 is an Armstrong number because 1**3 + 5**3 + 3**3 == 153.
'''

def is_armstrong(num: int) -> bool:
    numStr = str(num)
    numLen = len(numStr)
    sum_of_powers = sum(int(i) ** numLen for i in numStr)
    
    if sum_of_powers == num:
        return True
    else:
        return False


print("Example:")
print(is_armstrong(11))

# These "asserts" are used for self-checking
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True
assert is_armstrong(407) == True
assert is_armstrong(163) == False
assert is_armstrong(100) == False
assert is_armstrong(8208) == True
assert is_armstrong(930) == False
assert is_armstrong(4) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")