'''
Check if the given year is leap year. A year is a leap year if it is divisible by 4, 
except for end-of-century years which must be divisible by 400. 
This means that the year 2000 was a leap year, although 1900 was not.
'''
def is_leap_year(year: int) -> bool:
    leap_year = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
        else:
            leap_year = True
    # your code here
    return leap_year


print("Example:")
print(is_leap_year(1891))