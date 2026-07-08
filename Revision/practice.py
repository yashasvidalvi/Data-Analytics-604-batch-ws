#calculate total salary
import csv
file = open("Revision/employee_salary.csv","r")
dr = csv.DictReader(file)
total_salary = 0
for data in dr:
    sal = float(data['salary'])
    total_salary = total_salary+sal
print(total_salary)

#Maximum salary
import csv
file = open("Revision/employee_salary.csv","r")
dr = csv.DictReader(file)
max_sal = 0
name = ""
for data in dr:
    sal = float(data["salary"])
    if sal>max_sal:
        max_sal = sal
        name = data["emp_name"]
print(max_sal)
print(name)

#Minimum salary 
import csv
file = open("Revision/employee_salary.csv","r")
dr = csv.DictReader(file)
min_sal = float('inf')
name = ""
for data in dr:
    sal = float(data["salary"])
    if sal<min_sal:
        min_sal = sal
        name = data["emp_name"]
print(min_sal)
print(name)

#Average 
import csv
file = open("Revision/employee_salary.csv","r")
dr = csv.DictReader(file)
total_salary = 0
count =0

for data in dr:
    sal = float(data['salary'])
    total_salary = total_salary+sal
    count = count+1
average = total_salary/count
print(average)

# operation vale dusrya file madhe takne
import csv
file = open("Revision/employee_salary.csv","r")
dr = csv.DictReader(file)
new_file = open("Revision/operation_employee.csv","w")
dw = csv.DictWriter(new_file,['emp_id','emp_name','department','salary'])
for data in dr:
    if data["department"] == "Operation":
        dw.writerow(data)