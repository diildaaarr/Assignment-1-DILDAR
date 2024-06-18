import csv
with open ("myfilecsv.csv","r") as read:
    result=csv.reader(read)
    print(result)


