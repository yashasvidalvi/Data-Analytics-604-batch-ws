
from datetime import date, datetime


class Medicine:
    def __init__(self, medicine_id, name, category, manufacturer,
                 price, quantity, expiry_date):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity
        self.expiry_date = datetime.strptime(
            expiry_date, "%Y-%m-%d"
        ).date()

    def display(self):
        print(
            f"ID: {self.medicine_id} | Name: {self.name} | "
            f"Category: {self.category} | Manufacturer: {self.manufacturer} | "
            f"Price: ₹{self.price:.2f} | Stock: {self.quantity} | "
            f"Expiry: {self.expiry_date}"
        )


class Pharmacy:
    def __init__(self, name, location, minimum_stock=5):
        self.name = name
        self.location = location
        self.minimum_stock = minimum_stock
        self.medicines = {}
        self.total_sales = 0
        self.sales_records = []

    def add_medicine(self, medicine):
        if medicine.medicine_id in self.medicines:
            print("Error: Duplicate medicine ID.")
            return

        if medicine.price <= 0 or medicine.quantity < 0:
            print("Error: Invalid price or quantity.")
            return

        self.medicines[medicine.medicine_id] = medicine
        print("Medicine added successfully.")

    def update_medicine(self, medicine_id, price=None,
                        quantity=None, manufacturer=None):
        medicine = self.medicines.get(medicine_id)

        if medicine is None:
            print("Medicine not found.")
            return

        if price is not None:
            if price <= 0:
                print("Price must be positive.")
                return
            medicine.price = price

        if quantity is not None:
            if quantity < 0:
                print("Quantity cannot be negative.")
                return
            medicine.quantity = quantity

        if manufacturer is not None:
            medicine.manufacturer = manufacturer

        print("Medicine details updated.")

    def search_medicine(self, search_value):
        found = False

        for medicine in self.medicines.values():
            if (
                medicine.medicine_id == search_value
                or medicine.name.lower() == str(search_value).lower()
            ):
                medicine.display()
                found = True

        if not found:
            print("Medicine not found.")

    def restock(self, medicine_id, quantity):
        if quantity <= 0:
            print("Restock quantity must be positive.")
            return

        medicine = self.medicines.get(medicine_id)

        if medicine is None:
            print("Medicine not found.")
            return

        medicine.quantity += quantity
        print("Stock replenished successfully.")

    def purchase(self, medicine_id, quantity, discount_percent=0):
        medicine = self.medicines.get(medicine_id)

        if medicine is None:
            print("Medicine not found.")
            return

        if quantity <= 0:
            print("Purchase quantity must be positive.")
            return

        if not 0 <= discount_percent <= 100:
            print("Discount must be between 0 and 100.")
            return

        if medicine.expiry_date < date.today():
            print("Cannot sell expired medicine.")
            return

        if medicine.quantity < quantity:
            print("Insufficient stock.")
            return

        subtotal = medicine.price * quantity
        discount = subtotal * discount_percent / 100
        final_amount = subtotal - discount

        # Update stock only after all checks pass
        medicine.quantity -= quantity
        self.total_sales += final_amount

        bill = {
            "medicine": medicine.name,
            "quantity": quantity,
            "price_per_unit": medicine.price,
            "subtotal": subtotal,
            "discount": discount,
            "final_amount": final_amount
        }

        self.sales_records.append(bill)

        print("\n------ PHARMACY BILL ------")
        print("Pharmacy:", self.name)
        print("Medicine:", medicine.name)
        print("Quantity:", quantity)
        print(f"Price per unit: ₹{medicine.price:.2f}")
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Discount: ₹{discount:.2f}")
        print(f"Final amount: ₹{final_amount:.2f}")
        print("Remaining stock:", medicine.quantity)
        print("---------------------------")

    def show_inventory(self):
        print("\n------ MEDICINE INVENTORY ------")
        for medicine in self.medicines.values():
            medicine.display()

    def show_expired_medicines(self):
        print("\n------ EXPIRED MEDICINES ------")
        found = False

        for medicine in self.medicines.values():
            if medicine.expiry_date < date.today():
                medicine.display()
                found = True

        if not found:
            print("No expired medicines.")

    def show_low_stock(self):
        print("\n------ LOW STOCK MEDICINES ------")
        found = False

        for medicine in self.medicines.values():
            if medicine.quantity < self.minimum_stock:
                medicine.display()
                found = True

        if not found:
            print("No low-stock medicines.")

    def show_sales_report(self):
        print("\n------ SALES REPORT ------")
        for sale in self.sales_records:
            print(sale)

        print(f"Total revenue: ₹{self.total_sales:.2f}")


# Create pharmacy
pharmacy = Pharmacy("City Care Pharmacy", "Mumbai", 5)

# Create five medicine records
pharmacy.add_medicine(
    Medicine(101, "Paracetamol", "Tablet", "ABC Pharma",
             20, 50, "2027-12-31")
)
pharmacy.add_medicine(
    Medicine(102, "Cetirizine", "Tablet", "Health Pharma",
             30, 25, "2027-11-30")
)
pharmacy.add_medicine(
    Medicine(103, "Cough Syrup", "Syrup", "MediCare",
             120, 15, "2027-10-31")
)
pharmacy.add_medicine(
    Medicine(104, "Vitamin C", "Supplement", "Wellness",
             80, 3, "2027-09-30")
)
pharmacy.add_medicine(
    Medicine(105, "Antacid", "Tablet", "ABC Pharma",
             40, 20, "2027-08-31")
)

# Display inventory
pharmacy.show_inventory()

# Search by ID and name
pharmacy.search_medicine(101)
pharmacy.search_medicine("Vitamin C")

# Update existing medicine details
pharmacy.update_medicine(102, price=35)

# Make multiple purchases
pharmacy.purchase(101, 5, discount_percent=10)
pharmacy.purchase(103, 2, discount_percent=5)
pharmacy.purchase(102, 3)

# Demonstrate insufficient stock
pharmacy.purchase(104, 10)

# Restock medicine
pharmacy.restock(104, 20)

# Check stock and expiry
pharmacy.show_low_stock()
pharmacy.show_expired_medicines()

# Display updated inventory and revenue
pharmacy.show_inventory()
pharmacy.show_sales_report()
