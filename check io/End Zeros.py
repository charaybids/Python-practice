'''
Try to find out how many zeros a given number has at the end.
'''
def end_zeros(a: int) -> int:
    
    counter = 0 
    
    def divide_by_10(a: int) -> int:
        nonlocal counter
        if a % 10 == 0:
            counter += 1
            return divide_by_10(a // 10)
        else:
            return a
    
    if a != 0:
        divide_by_10(a)
    else:
        counter = 1
        
    return counter


print("Example:")
print(end_zeros(10))