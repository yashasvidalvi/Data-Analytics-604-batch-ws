# import numpy as np
# salary = [1000,2000,3000,4000,5000]
# salary = np.array(salary)
# print(salary/2) 

#Calculate the total revenue collected by the institute from student fee payments.
import csv
file = open("Revision/students_record.csv","r")

reader_obj = csv.DictReader(file)
rev = 0
for data in reader_obj:
    rev = rev +int(data['total_fee'])
print(rev)


#Identify the most popular course based on the highest number of student admissions.
file = open("Revision/students_record.csv","r")
reader_obj = csv.DictReader(file)
count = {}
for data in reader_obj:
    course = data['course']
    count[course] = count.get(course, 0)+1
    most_popular_course = max(count, key = count.get)
    print("Most popular course is:", most_popular_course, "with", count[most_popular_course], "admissions.")


#find the branch that generated the highest revenue from fee colletions.
file = open("Revision/students_record.csv","r")
reader_obj = csv.DictReader(file)
revenue = {}
for data in reader_obj:
    branch = data['branch']
    total_fee = int(data['total_fee'])
    revenue[branch] = revenue.get(branch, 0)+total_fee
    highest_revenue_branch = max(revenue,key = revenue.get)
    print("Branch with highest revenue is:", highest_revenue_branch, "with revenue of", revenue[highest_revenue_branch])


#calculate the total pending fees for each branch
pending_fee = {}
file = open("Revision/students_record.csv","r")
reader_obj = csv.DictReader(file)

for data in reader_obj:
    branch = data["branch"]
    pending = int(data["total_fee"]) - int(data["paid_fees"])

    pending_fee[branch] = pending_fee.get(branch, 0) + pending

print("Pending Fees Branch-wise")

for branch, amount in pending_fee.items():
    print(branch, "=", amount)
    print("Total pending fees for branch", branch, "is:", amount)


#Compare course-wise revenue and identify the highest and lowest revenue-generating course.
revenue = {}
file = open("Revision/students_record.csv","r")
reader_obj = csv.DictReader(file)

for data in reader_obj:
    course = data["course"]
    total_fee = int(data["total_fee"])
    revenue[course] = revenue.get(course, 0) + total_fee

highest_revenue_course = max(revenue, key=revenue.get)
lowest_revenue_course = min(revenue, key=revenue.get)

print("Course-wise Revenue:")
for course, amount in revenue.items():
    print(course, "=", amount)
    
print("Highest revenue-generating course:", highest_revenue_course, "with revenue of", revenue[highest_revenue_course])
print("Lowest revenue-generating course:", lowest_revenue_course, "with revenue of", revenue[lowest_revenue_course])

