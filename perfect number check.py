'''
A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. 
For example, 28 is a perfect number because its divisors are 1, 2, 4, 7, and 14, and their sum is 28.
'''

def is_perfect(n: int) -> bool:
    
    divisors = []
    
    for i in range(1, n):
        if n % i == 0 and i != n:
            divisors.append(i)
    
    if n == sum(divisors):
        return True
    # your code here
    return False


print("Example:")
print(is_perfect(6))