with open ("myfile.txt","w") as p:
    p.flush()

    while(True):
        str = input("enter the line")
        if(str!=""):
            p.write(str)


        else:
            r = open("myfile.txt", "r")
            result = r.read()
            print(result)
            r.close()
            break



