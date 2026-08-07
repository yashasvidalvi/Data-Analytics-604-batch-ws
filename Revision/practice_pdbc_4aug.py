# from mysql import connector

# connection = connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "diksha",
#     database = "product_db",
#     port = 3306
# )

# cursor = connection.cursor()

# cursor.execute("select * from products")
# products = cursor.fetchall()

# for pid,pname,category,mrp,rating in products:
#     if rating >3:
#         cursor.execute("insert into rating1(pid,pname) values(%s,%s)",(pid,pname))
#     else:
#         cursor.execute("insert into rating2(pid,pname) values(%s,%s)",(pid,pname))
# connection.commit()
# print("Data Inserted successfully")

# Second Task like above
from mysql.connector import connect
connection = connect(
    user = "root",
    password = "diksha",
    host = "localhost",
    port = 3306,
    database = "product_db"
)

cursor = connection.cursor()
q = "select pid,pname,rating from products"
cursor.execute(q)
data = cursor.fetchall()
for record in data:
    rating = record[2]
    pid = record[0]
    pname = record[1]
    if rating >3:
        q = "insert into rating1(pid,pname) values(%s,%s)"
        cursor.execute(q,(pid,pname))
        connection.commit()
    else:
        q = "insert into rating2(pid,pname) values(%s,%s)"
        cursor.execute(q,(pid,pname))
        connection.commit()


#Task 2
# from mysql.connector import connect
# connection = connect(
#     user = "root",
#     password = "diksha",
#     host = "localhost",
#     port = 3306,
#     database = "product_db"
# )

# cursor = connection.cursor()
# q = "select category,mrp from products"
# cursor.execute(q)
# data = cursor.fetchall()
# for record in data:
#     category = record[0]
#     mrp = record[1]
#     if category == "electronics":
#         q = "update products set mrp = mrp*1.10"
#         cursor.execute(q)
#         connection.commit()
#     elif category == "furniture":
#         q = "update products set mrp = mrp*1.05"
#         cursor.execute(q)
#         connection.commit()
#     else:
#         q = "update products set mrp = mrp*1.02"
#         cursor.execute(q)
#         connection.commit()
