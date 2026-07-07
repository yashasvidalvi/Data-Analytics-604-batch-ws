# import csv
# file = open("student_records.csv","r")
# rd = csv.reader(file)
# all_lines = list(rd)
# for line in all_lines[1:]:
#     if float(line[-1])<40:
#         print(line[1])

# import csv
# file = open("student_records.csv","a")
# wt = csv.writer(file)
# roll = input("Enter Roll: ")
# name = input("Enter Name: ")
# marks = input("Enter Marks: ")
# wt.writerow([roll,name,marks])


# file = open("student_records.csv","a")
# wt = csv.writer(file)
# wt.writerows([[7,"Shruti Satam",70],[8,"Priyanka Sawant",80],[9,"Siddhi Parab",90]])

# import csv
# file = open("student_records.csv","r")
# dr = csv.DictReader(file)
# for data in dr:
#     if float(data['Marks'])>40:
#         print(data['Name'])

import csv
file = open("student_records.csv","a")
dw = csv.DictWriter(file,["Roll","Name","Marks"])
dw.writerow({"Roll":11,"Name":"Saniya Chavan","Marks":60})