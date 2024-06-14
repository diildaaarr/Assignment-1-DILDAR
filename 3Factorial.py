# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Taking a number as input from the user
number = int(input("Enter a number: "))

# Checking if the number is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculating the factorial of the number
    result = factorial(number)
    # Printing the result
    print(f"The factorial of {number} is {result}.")
