from mysql import connector
conn = connector.connect(
    user="root",
    password="diksha",
    host="localhost",
    port=3306,
)
#print("Connected...")

cur = conn.cursor()
#cur.execute("create database Admission_db_604")
# cur.execute("show databases")
# for i in cur:
#     print(i)

cur.execute("use Admission_db_604")
# cur.execute("show tables")
# for i in cur:
#     print(i)

#cur.execute("create table student_details(roll int primary key, name varchar(70) not null,city varchar(60))")

# cur.execute("insert into student_details values(1,'Yashasvi','Pune')")
# conn.commit()


# cur.execute("insert into student_details values(2,'Diksha','Mumbai'),(3,'Shreya','Nashik')")
# conn.commit()

# cur.execute("select * from student_details")
# for i in cur:
#     print(i)


cur.execute("select * from student_details")
data = cur.fetchall()
print(data)
