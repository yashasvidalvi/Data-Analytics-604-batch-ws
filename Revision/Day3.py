#Department wise data filter
import csv
file = open("Revision/employee_salary.csv","r")
dr = csv.DictReader(file)

new_file = open("Revision/operation_employee.csv","w")
dw = csv.DictWriter(new_file,['emp_id','emp_name','department','salary'])
dw.writeheader()

new_file1 = open("Revision/HR_employee.csv","w")
dw1 = csv.DictWriter(new_file1,['emp_id','emp_name','department','salary'])
dw1.writeheader()

new_file2 = open("Revision/Placement_employee.csv","w")
dw2 = csv.DictWriter(new_file2,['emp_id','emp_name','department','salary'])
dw2.writeheader()

for data in dr:
    if data["department"] == "Operation":
        dw.writerow(data)
    elif data['department'] == "HR":
        dw1.writerow(data)
    else:
        dw2.writerow(data)

#count char in string
name = "Yashasvi"
count = {}
for char in name:
    if char not in count:
        count[char]=1
    else:
        count[char] = count[char]+1
print(count)