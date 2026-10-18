class Patient:
    hospital_name = "City Care Hospital"

    def __init__(self,patient_id,patient_name,age,disease,room_number,total_bill):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.room_number = room_number
        self.total_bill = total_bill

    def display_patient_details(self):
        print("Hosptial Name: ",Patient.hospital_name)
        print("Patient ID: ",self.patient_id)
        print("Patient Name: ",self.patient_name)
        print("Age: ",self.age)
        print("Disease: ",self.disease)
        print("Room Number: ",self.room_number)
        print("Total Bill: ₹",self.total_bill)
        print("-"*35)

    def update_disease(self,new_disease):
        self.disease = new_disease
        print("Disease updated successfully")

    def add_bill(self, amount):
        if amount >0:
            self.total_bill += amount
            print("Bill updated successfully")
        else:
            print("Amount must be positive")

    @classmethod
    def change_hospital_name(cls,new_name):
        cls.hospital_name = new_name
        print("Hospital name changed successfully")

    @staticmethod
    def check_age_validity(age):
        return isinstance(age,int) and 0<=age<=120

    def __str__(self):
        return (
            f"Patient ID: {self.patient_id},"
            f"Name:{self.patient_name},"
            f"Age:{self.age},"
            f"Disease:{self.disease}"
        )

# Step 3: Create three patient objects
p1 = Patient(1,"Amit",35,"Fever",101,5000)
p2 = Patient(2,"Sneha",28,"Migraine",102,7500)
p3 = Patient(1,"Rahul",45,"Asthma",103,10000)

# Step 4: Display all patients
print("All Patient Details")
p1.display_patient_details()
p2.display_patient_details()
p3.display_patient_details()

# Step 5: Update a patient's disease
print("\nUpdating Disease")
p1.update_disease("Viral Fever")
p1.display_patient_details()

# Step 6: Add a charge to another patient's bill
print("\nAdding Bill")
p2.add_bill(1500)
p2.display_patient_details()

# Step 7: Change the hospital name
print("\nChanging Hospital Name")
Patient.change_hospital_name("Lifeline Hospital")
p1.display_patient_details()

# Step 8: Check age validity
print("\nAge Validation")
print("Age 25:", Patient.check_age_validity(25))
print("Age 150:", Patient.check_age_validity(150))

# Step 9: Test the __str__() method
print("\nPATIENT OBJECT")
print(p1)