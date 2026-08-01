from mysql import connector
conn = connector.connect(
    user = "root",
    password = "diksha",
    host = "localhost",
    port = 3306,
    database = "hotel_raj_db"
)
cur = conn.cursor()

print("HOTEL RAJ".center(105,"-"))

cur.execute("select sr,item_name from menu")
menu = cur.fetchall()

orders = {}
while True:
    print("MENU".center(50,"-"))
    for sr,name in menu:
        print(f'{sr}.{name}')
    print("-"*50)
    item_no = int(input("Enter your choice: "))
    qun = int(input("Enter quantity: "))
    orders[item_no] = qun
    con = input("Do you want to continue:(y/n): ")
    if con =="n":
        break
print("-"*105)
print(f'|{"SR":^20}|{"ITEM_NAME":^20}|{"QUANTITY":^20}|{"PRICE":^20}|{"AMOUNT":^20}|')
print("-"*105)
total = 0
for sr,qun in orders.items():
    cur.execute(f'select item_name,price from menu where sr = {sr}')
    data = cur.fetchall()
    item_name = data[0][0]
    price = data[0][1]
    amount = price*qun
    print(f'|{sr:^20}|{item_name:^20}|{qun:^20}|{price:^20}|{amount:^20}|')
    print("-"*105)
#     print(f'|{sr:^20}|{item_name:^20}|{qun:^20}|{price:^20}|{amount:^20}|')
# insert_query = """
# INSERT INTO bill_details
# (item_no, item_name, quantity, price, amount)
# VALUES (%s,%s,%s,%s,%s)
# """
# values = (sr, item_name, qun, price, amount)
# cur.execute(insert_query, values)
# conn.commit()
    total = total+amount
print(f'Total Bill Amount: {total}')