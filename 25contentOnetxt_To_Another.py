p1=open("myfile.txt","r")
result=p1.read()
with open("nextfile.txt","w") as p:
    p.write(result)

p1.close()