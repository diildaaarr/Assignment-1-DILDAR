str1=input("enter the string ")
str2=input("enter the string ")
def  checkAnagram(str1,str2):
    dic1={}
    dic2={}
    for i in str1:
        if i in dic1:
            dic1[i]+=1
        else:
            dic1[i]=1

    for i in str2:
        if i in dic2:
            dic2[i]+=1
        else:
            dic2[i]=1

    if(dic1==dic2):
        print("these are anagrams")
    else:
        print("these are not anagrams")
checkAnagram(str1,str2)