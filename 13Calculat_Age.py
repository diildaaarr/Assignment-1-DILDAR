from datetime import datetime

# Current year
current_year = datetime.now().year

# Taking the birth year as input from the user
birth_year = int(input("Enter your birth year: "))

# Calculating the age
age = current_year - birth_year

# Printing the age
print("Your age is:", age)
