# Taking the main string as input from the user
main_string = input("Enter the main string: ")

# Taking the substring as input from the user
substring = input("Enter the substring to check: ")

# Checking if the substring is present in the main string
if substring in main_string:
    print("The substring ",substring ,"is present in the main string.")
else:
    print("The substring ",substring,"is not present in the main string.",)
