# Defining the file name
file_name = "myfile.txt"

try:
    # Opening the file in read mode
    with open(file_name, "r") as file:
        # Reading the content of the file
        content = file.read()

    # Printing the content to the console
    print("The content of the file is:")
    print(content)
except FileNotFoundError:
    print("The file",file_name," does not exist.")
