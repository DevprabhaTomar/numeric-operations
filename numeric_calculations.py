# User-defined function
def add_and_subtract(a, b):
#def is used to define a function.
#add_and_subtract is the name of the function.
    addition = a + b
    difference = a - b
    return addition, difference

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Function call
sum_result, diff_result = add_and_subtract(num1, num2)

# Displaying results
print("Addition:", sum_result)
print("Difference:", diff_result)
