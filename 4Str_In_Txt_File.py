# Taking a string input from the user
user_input = input("Enter a string to write to the file: ")

# Defining the file name
file_name = "myfile.txt"

# Writing the string to the file
with open(file_name, "w") as file:
    file.write(user_input)

print(f"The string has been written to ",file_name)
