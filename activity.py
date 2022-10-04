"""
Activity:
1. Accept a year input from the user and determine if it is a leap year or not.
2. Accept two numbers (row and col) from the user and create a grid of asterisks using the two numbers (row and col).

Stretch Goal:
1. Add a validation for the leap year input:
- Strings are not allowed for inputs
- No zero or negative values
"""
Year = int(input("Enter the number: "))  

if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year")   
else:  
    print ("Given Year is not a leap Year")  


Rows_num = int(input("Enter number of row: ")) 
Column_num= int(input("Enter number of column: ")) 


for x in range(Row_num):
    for y in range(Column_num):
        print('*',end = ' ')
    print()