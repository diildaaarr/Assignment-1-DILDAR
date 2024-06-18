print(" press 1 to give input as celsius")
print(" press 2 to give input as fahrenheit")
num=int(input("enter the number "))
n=int(input("enter the temperature "))
def celsiusToFahrenheit(n):
    result=((n*9)/5)+32
    print("the ouput in fahrenheit is ",result)

def fahrenheitToCelcius(n):
    result=((n-32)*5)/9
    print("the ouput in celsius is ",result)


if (num == 1):
    celsiusToFahrenheit(n)
else:
    fahrenheitToCelcius(n)



