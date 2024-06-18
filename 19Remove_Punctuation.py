punctuation = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
str1 = input("Enter the string: ")


for char in punctuation:
    str1 = str1.replace(char, '')

print(str1)
