# class Rectangle:
#     'width'== 9.5
#     'height'== 6.5
#     'length' == 50
#     def __init__(self,len,he):
#         self.length = len
#         self.height = he

#     def cal_area(self):
#         area = self.height*self.length
#         return area
#     def cal_perimeter(self):
#         peri = 2*(self.length+self.height)
#         return peri    

# r1 = Rectangle(35,20)
# print(r1.cal_area())
# print(r1.cal_perimeter())

import csv
class Bank:
    def __init__(self):
        pass

    def create_account(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        balance = input("Enter Balance: ")

        file = open("Revision/accounts.csv","r")
        dr = csv.DictReader(file)
        account_no = 123456101 + len(list(dr))

        file = open("Revision/accounts.csv","a",newline="")
        dw = csv.DictWriter(file, fieldnames=['account_no','name','email','balance'])
        dw.writerow({'account_no':f'{account_no}','name':name,'email':email,'balance':balance})
        print("Account Created Successfully....")
        print("Your Account Number is :",account_no)
    
    def show_account_details(self):
        details = input("Enter Your Account number: ")
        file = open("Revision/accounts.csv","r")
        dr = csv.DictReader(file)
        
        found = False
        for data in dr:
            if data["account_no"] == details:
                print("----- Account Details -----")
                print("Account Number: ",data["account_no"])
                print("Name: ",data["name"])
                print("Email: ",data["email"])
                print("Balance: ",data["balance"])
                found = True
                break
        if found == False:
            print("Invalid Account Number")

emp1 = Bank()
emp1.create_account()
emp1.show_account_details()
