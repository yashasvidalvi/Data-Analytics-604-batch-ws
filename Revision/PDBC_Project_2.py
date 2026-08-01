from mysql.connector import connect
def connection():
    conn = connect(
        user = "root",
        password = "diksha",
        host = "localhost",
        port = 3306,
        database = "management_system_db"
    )
    return conn
conn = connection()
cur = conn.cursor()
def login(cur):
    username = input("Username: ")
    password = input("Password: ")
    cur.execute("select username,password from ms_users")
    all_users = cur.fetchall()
    all_users = dict(all_users)
    if username in all_users and all_users[username] == password:
        return True
    else:
        return False
# print(login(cur))

def add_student(cur):
    reg = int(input("Enter reg: "))
    name = input("Name: ")
    city = input("city: ")
    mobile = int(input("mobile: "))
    email = input("email: ")
    cur.execute(f"insert into student_details values({reg},'{name}','{city}','{mobile}','{email}')")
    conn.commit()
#add_student(cur)

def show_details(cur):
    reg = int(input("Reg Number:"))
    cur.execute('select * from student_details where reg = %s',(reg,))
    data = cur.fetchall()
    print('-'*105)
    print(f'|{"Reg No":^20}|{"Student Name":^20}|{"City":^20}|{"Mobile":^20}|{"Email":^20}|')
    print('-'*105)
    print(f'|{data[0][0]:^20}|{data[0][1]:^20}|{data[0][2]:^20}|{data[0][3]:^20}|{data[0][4]:^20}|')
    print('-'*105)
#show_details(cur)

def add_marks(cur):
    reg = int(input("Reg: "))
    t1 = float(input("Enter Test1 Marks: "))
    t2 = float(input("Enter Test2 Marks: "))
    t3 = float(input("Enter Test3 Marks: "))
    cur.execute(f"insert into student_marks values({reg},{t1},{t2},{t3})")
    conn.commit()
#add_marks(cur)

def cal_percentage(cur):
    reg = int(input("Reg: "))
    cur.execute(f"select test1,test2,test3 from student_marks where roll = '{reg}'")
    data = cur.fetchall()
    t1,t2,t3 = data[0]
    obt = t1+t2+t3
    per = obt/300 * 100
    return per
#print(cal_percentage(cur))

def result(cur):
    per = cal_percentage(cur)
    if per>40:
        return "Pass"
    else:
        return "Fail"

print("Welcome To Management System".center(100,'-'))
user = login(cur)
if user:
    while True:
        print(''' 
            1. Add Student
            2. Show details
            3. add Marks
            4. cal percentage
            5. show result
            ''')
        ch = int(input("Enter Your Choice: "))
        if ch == 1:
            add_student(cur)
        elif ch == 2:
            show_details(cur)
        elif ch == 3:
            add_marks(cur)
        elif ch == 4:
            per = cal_percentage(cur)
            print(per)
        elif ch == 5:
            show_details(cur)
else:
    print("Invalid Username and Password")