"""
Activity:
1. Accept a year input from the user and determine if it is a leap year or not.
2. Accept two numbers (row and col) from the user and create a grid of asterisks using the two numbers (row and col).

Stretch Goal:
1. Add a validation for the leap year input:
- Strings are not allowed for inputs
- No zero or negative values
"""
enter_div_num = int(input("Please enter a number:\n"))
if enter_div_num == 1:
	print(f"{enter_div_num} is a not a leap year!")
elif enter_div_num == 2:
	print(f"{enter_div_num} is a leap year!")
else:
	print(f"{enter_div_num} is not a leap year nor a leap year!")


Rows_num = int(input("Enter number of row: ")) 
Column_num= int(input("Enter number of column: ")) 


for x in range(Rows_num):
    for y in range(Column_num):
        print('*',end = ' ')
    print()