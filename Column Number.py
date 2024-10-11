'''
Given a string that represents the column title as appears in an Excel sheet, return its corresponding column number.

But how does the Excel column numbering actually work? 
Well, the column number is like decimal number, but with base (radix) 26 and "digits" A-Z.
'''

def column_number(name: str) -> int:
    column_number = 0
  
    for letter in name:
        #ord() function returns the Unicode code point of the character
        column_number = column_number * 26 + (ord(letter) - 64)
    
    return column_number


print("Example:")
print(column_number("AA"))