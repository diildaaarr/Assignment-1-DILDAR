lst=eval(input("enter the list of integers only "))
num=int(input("enter the number check "))
def checkOccurence(lst,num):
    count=0;
    for i in lst:
        if(i==num):
            count+=1
    return count

num1=checkOccurence(lst,num)
print("the occurence of ",num," is ",num1)