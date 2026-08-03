# from mysql import connector
# connection = connector.connect(
#     user = "root",
#     password = "diksha",
#     host = "localhost",
#     port = 3306,
#     database = "employee_db"
# )
# cursor = connection.cursor(dictionary = True)
# query = "select * from employee"
# cursor.execute(query)
# employees = cursor.fetchall()
# for employee in employees:
#     sal = employee['empsalary']
#     empname = employee['empname']
#     empid = employee['empid']
#     if int(sal) >10000:
#         query = (f"insert into emp_high_salary(empname) values ('{empname}')")
#         print(query)
#         cursor.execute(query)
#         connection.commit()
#     else:
#         query = (f"insert into emp_low_salary(empname) values ('{empname}')")
#         print(query)
#         cursor.execute(query)
#         connection.commit()

# Task 2

from mysql import connector

conn = connector.connect(
    host="localhost",
    user="root",
    password="diksha",          
    database="employee_db"    
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS emp1(
    empid INT PRIMARY KEY,
    empname VARCHAR(50),
    empsalary INT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS emp2(
    empid INT PRIMARY KEY,
    empname VARCHAR(50),
    empsalary INT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS emp3(
    empid INT PRIMARY KEY,
    empname VARCHAR(50),
    empsalary INT
)
""")

cur.execute("SELECT * FROM emp")
records = cur.fetchall()

for empid, empname, empsalary in records:

    if empname.upper().startswith("R"):
        cur.execute(
            "INSERT INTO emp1(empid, empname, empsalary) VALUES (%s,%s,%s)",
            (empid, empname, empsalary)
        )

    elif empname.upper().startswith("P"):
        cur.execute(
            "INSERT INTO emp2(empid, empname, empsalary) VALUES (%s,%s,%s)",
            (empid, empname, empsalary)
        )

    else:
        cur.execute(
            "INSERT INTO emp3(empid, empname, empsalary) VALUES (%s,%s,%s)",
            (empid, empname, empsalary)
        )

conn.commit()

print("Data transferred successfully.")