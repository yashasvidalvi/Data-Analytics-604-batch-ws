#department wise data filter
import csv
file = open("revision/employee_salary.csv","r")
dr = csv.DictReader(file)
dep_data = {}
for data in dr:
    dep = data["department"]
    if dep not in dep_data:
        dep_data[dep] = []
    dep_data[dep].append(data)
for dep,data in dep_data.items():
    filename = dep+'.csv'
    file1 = open(filename,"w")
    dw = csv.DictWriter(file1,fieldnames = data[0].keys())
    dw.writeheader()
    dw.writerows(data)

#department wise minimum maximum salary
import csv
file = open("revision/employee_salary.csv","r")
dr = csv.DictReader(file)
emp_sum = {}
for data in dr:
    dep = data["department"]
    sal = data['salary']
    if dep not in emp_sum:
        emp_sum[dep] = {"min_sal":sal,"max_sal":sal}
    else:
        if sal<emp_sum[dep]['min_sal']:
            emp_sum[dep]['min_sal'] = sal
        if sal>emp_sum[dep]['max_sal']:
            emp_sum[dep]['max_sal'] = sal     
print(emp_sum)

file1 = open("revision/salary_summary.csv","a")
w = csv.writer(file1)
w.writerow(["department","min_salary","max_salary"])
for dep,data in emp_sum.items():
    w.writerow([dep,data["min_sal"],data["max_sal"]])