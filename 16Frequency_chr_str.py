str=input("enter the string ")
sett=set()
for i in str:
    sett.add(i)

for j in sett:
    count=0
    for k in range(0,len(str)):
        if(str[k]==j):
            count+=1
    print("the frequency of ",j, " is ", count)

