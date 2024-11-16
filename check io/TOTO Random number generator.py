from random import randint
import pandas as pd

def generate_num() -> int:
    return randint(1, 49)

def generate_numarray(n: int, num_list: list[int]) -> list[int]:    
    num_list = list(dict.fromkeys(num_list))# Remove duplicates
    
    while len(num_list) < n:
        num_list.append(generate_num())
        num_list = list(dict.fromkeys(num_list))# Remove more duplicates
    
    return num_list

for i in range(10):
    generated_list = generate_numarray(8, [generate_num() for _ in range(6)])
    generated_list.sort()
    print(generated_list)


'''
********DO NOT UNCOMMENT THIS BLOCK OF CODE********
# Output the generated list to a csv file 
data = []
for i in range(50000):
    generated_list = generate_numarray(6, [generate_num() for _ in range(6)])
    generated_list.sort()
    data.append(generated_list)

df = pd.DataFrame(data, columns=[f'Number_{i+1}' for i in range(6)])
df.to_csv('generated_numbers.csv', index=False)
print('File generated successfully')
'''
    
    
    