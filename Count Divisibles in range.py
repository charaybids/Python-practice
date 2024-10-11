'''
Given two integers, n and k, the task is to count how many numbers between 1 and n (inclusive) are divisible by k.
'''

def count_divisible(n: int, k: int) -> int:
    if k == 0:
        raise ValueError("k cannot be zero")
    if n < 0 or k < 0:
        raise ValueError("n and k must be non-negative")
    
    return n // k

'''
# No for loops allowed when numbers get too large
def count_divisible(n: int, k: int) -> int:
    counter = 0
    
    for i in range(1, n + 1):
        if i % k == 0:
            counter += 1
    
    return counter
'''

print("Example:")
print(count_divisible(2, 1))