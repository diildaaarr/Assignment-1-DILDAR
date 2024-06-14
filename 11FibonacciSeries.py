
def fibonacci(n):
    lst = [0,1]

    for i in range(2,n+1):
        m=lst[-1]+lst[-2]
        lst.append(m)
    for i in lst:
        print(i ," ")

n=int(input("enter the no "))
fibonacci(n)

