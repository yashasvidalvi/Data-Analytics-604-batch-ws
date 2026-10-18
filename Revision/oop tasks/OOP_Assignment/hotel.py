
from datetime import datetime, timedelta


class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.available = True


class Guest:
    def __init__(self, guest_id, name, age, contact, address):
        self.guest_id = guest_id
        self.name = name
        self.age = age
        self.contact = contact
        self.address = address


class Hotel:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = {}
        self.guests = {}
        self.bookings = {}
        self.next_booking_id = 1
        self.total_revenue = 0

    def add_room(self, room):
        if room.room_number in self.rooms:
            print("Duplicate room number.")
            return

        if room.price <= 0:
            print("Room price must be positive.")
            return

        self.rooms[room.room_number] = room
        print("Room added:", room.room_number)

    def register_guest(self, guest):
        if guest.guest_id in self.guests:
            print("Duplicate guest ID.")
            return False

        if guest.age < 0 or not guest.contact.strip():
            print("Invalid guest details.")
            return False

        self.guests[guest.guest_id] = guest
        print("Guest registered:", guest.name)
        return True

    @staticmethod
    def parse_date(value):
        return datetime.strptime(value, "%Y-%m-%d").date()

    def is_room_available(self, room_number, check_in, check_out,
                           exclude_booking=None):
        if room_number not in self.rooms:
            return False

        for booking_id, booking in self.bookings.items():
            if booking_id == exclude_booking:
                continue

            if booking["room_number"] != room_number:
                continue

            if booking["status"] == "Cancelled":
                continue

            # Overlap exists if the date ranges intersect.
            if check_in < booking["check_out"] and (
                check_out > booking["check_in"]
            ):
                return False

        return True

    def book_room(self, guest_id, room_number, start, end):
        if guest_id not in self.guests:
            print("Guest not registered.")
            return None

        if room_number not in self.rooms:
            print("Room does not exist.")
            return None

        try:
            check_in = self.parse_date(start)
            check_out = self.parse_date(end)
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")
            return None

        if check_in >= check_out:
            print("Check-out must be after check-in.")
            return None

        if not self.is_room_available(
            room_number, check_in, check_out
        ):
            print("Room is unavailable for these dates.")
            return None

        booking_id = self.next_booking_id
        self.next_booking_id += 1

        self.bookings[booking_id] = {
            "guest_id": guest_id,
            "room_number": room_number,
            "check_in": check_in,
            "check_out": check_out,
            "status": "Booked",
            "services": 0.0,
            "discount": 0.0,
            "paid": 0.0
        }

        print("Booking successful. Booking ID:", booking_id)
        return booking_id

    def modify_booking(self, booking_id, start, end):
        booking = self.bookings.get(booking_id)

        if booking is None or booking["status"] != "Booked":
            print("Only existing bookings can be modified.")
            return

        try:
            check_in = self.parse_date(start)
            check_out = self.parse_date(end)
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")
            return

        if check_in >= check_out:
            print("Invalid booking duration.")
            return

        if not self.is_room_available(
            booking["room_number"], check_in, check_out,
            exclude_booking=booking_id
        ):
            print("Room unavailable for the modified dates.")
            return

        booking["check_in"] = check_in
        booking["check_out"] = check_out
        print("Booking modified successfully.")

    def cancel_booking(self, booking_id):
        booking = self.bookings.get(booking_id)

        if booking is None or booking["status"] != "Booked":
            print("Booking cannot be cancelled.")
            return

        if booking["paid"] > 0:
            print("Refund any advance payment before cancellation.")
            return

        booking["status"] = "Cancelled"
        print("Booking cancelled successfully.")

    def check_in(self, booking_id):
        booking = self.bookings.get(booking_id)

        if booking is None or booking["status"] != "Booked":
            print("Invalid booking for check-in.")
            return

        today = datetime.today().date()

        if today != booking["check_in"]:
            print("Check-in is allowed only on the booked date.")
            return

        booking["status"] = "Checked In"
        self.rooms[booking["room_number"]].available = False
        print("Guest checked in successfully.")

    def add_service_charge(self, booking_id, amount):
        booking = self.bookings.get(booking_id)

        if booking is None or booking["status"] != "Checked In":
            print("Guest must be checked in first.")
            return

        if amount <= 0:
            print("Service charge must be positive.")
            return

        booking["services"] += amount
        print("Service charge added.")

    def check_out(self, booking_id, discount_percent=0):
        booking = self.bookings.get(booking_id)

        if booking is None or booking["status"] != "Checked In":
            print("Check-out requires a valid check-in.")
            return

        if not 0 <= discount_percent <= 100:
            print("Invalid discount percentage.")
            return

        today = datetime.today().date()

        if today < booking["check_in"]:
            print("Invalid check-out date.")
            return

        room = self.rooms[booking["room_number"]]
        nights = (today - booking["check_in"]).days

        # At least one night is charged.
        nights = max(1, nights)

        accommodation = room.price * nights
        discount = accommodation * discount_percent / 100
        total = accommodation - discount + booking["services"]

        booking["discount"] = discount
        booking["total"] = total
        booking["nights"] = nights
        booking["status"] = "Checked Out"
        room.available = True

        print("\n========== HOTEL INVOICE ==========")
        print("Hotel:", self.name)
        print("Location:", self.location)
        print("Guest:", self.guests[booking["guest_id"]].name)
        print("Guest ID:", booking["guest_id"])
        print("Room:", room.room_number, "-", room.room_type)
        print("Price per night: ₹", room.price)
        print("Check-in:", booking["check_in"])
        print("Check-out:", today)
        print("Nights:", nights)
        print("Accommodation: ₹", accommodation)
        print("Additional services: ₹", booking["services"])
        print("Discount: ₹", discount)
        print("Final bill: ₹", total)
        print("Paid so far: ₹", booking["paid"])
        print("Outstanding: ₹", total - booking["paid"])
        print("===================================")

    def make_payment(self, booking_id, amount):
        booking = self.bookings.get(booking_id)

        if booking is None or "total" not in booking:
            print("A bill must be generated before payment.")
            return

        if amount <= 0:
            print("Payment must be positive.")
            return

        outstanding = booking["total"] - booking["paid"]

        if amount > outstanding:
            print("Payment exceeds outstanding balance.")
            return

        booking["paid"] += amount
        self.total_revenue += amount

        print("Payment received: ₹", amount)
        print("Outstanding balance: ₹",
              booking["total"] - booking["paid"])

    def show_available_rooms(self):
        print("\n------ AVAILABLE ROOMS ------")
        for room in self.rooms.values():
            if room.available:
                print(
                    room.room_number, room.room_type,
                    "₹", room.price, "per night"
                )

    def show_bookings(self):
        print("\n------ BOOKINGS ------")
        for booking_id, booking in self.bookings.items():
            guest = self.guests[booking["guest_id"]]
            print(
                "Booking:", booking_id,
                "| Guest:", guest.name,
                "| Room:", booking["room_number"],
                "| Dates:", booking["check_in"],
                "to", booking["check_out"],
                "| Status:", booking["status"]
            )

    def revenue_report(self):
        print("\nTotal payments received: ₹", self.total_revenue)


# Create hotel
hotel = Hotel("Sunrise Hotel", "Mumbai")

# Add five rooms
hotel.add_room(Room(101, "Single", 1500))
hotel.add_room(Room(102, "Double", 2500))
hotel.add_room(Room(103, "Deluxe", 4000))
hotel.add_room(Room(104, "Suite", 6000))
hotel.add_room(Room(105, "Double", 2500))

# Register three guests
hotel.register_guest(
    Guest(1, "Amit", 30, "9876543210", "Mumbai")
)
hotel.register_guest(
    Guest(2, "Sneha", 25, "9876543211", "Pune")
)
hotel.register_guest(
    Guest(3, "Rahul", 35, "9876543212", "Nashik")
)

# Book rooms using dates in YYYY-MM-DD format.
# Example booking dates are in the future.
b1 = hotel.book_room(1, 101, "2027-01-10", "2027-01-13")
b2 = hotel.book_room(2, 102, "2027-01-10", "2027-01-12")
b3 = hotel.book_room(3, 103, "2027-01-15", "2027-01-17")

# Try booking the same room for overlapping dates
hotel.book_room(2, 101, "2027-01-12", "2027-01-14")

# Modify a booking
hotel.modify_booking(b2, "2027-01-11", "2027-01-13")

# Cancel a booking with no advance payment
hotel.cancel_booking(b3)

# Demonstrate available rooms and current bookings
hotel.show_available_rooms()
hotel.show_bookings()

# For a real check-in, use a booking whose check-in date is today.
# After check-in, add services, check out, and make payments.
# Example workflow is provided below.


# Generate dates dynamically
today = datetime.today().date()
start = today.strftime("%Y-%m-%d")
end = (today + timedelta(days=3)).strftime("%Y-%m-%d")

# Create multiple bookings
b1 = hotel.book_room(1, 101, start, end)
b2 = hotel.book_room(2, 102, start, end)
b3 = hotel.book_room(3, 103, start, end)

# Try booking an already reserved room for overlapping dates
hotel.book_room(2, 101, start, end)

# Modify a booking
new_start = (today + timedelta(days=1)).strftime("%Y-%m-%d")
new_end = (today + timedelta(days=4)).strftime("%Y-%m-%d")
hotel.modify_booking(b2, new_start, new_end)

# Cancel a booking
hotel.cancel_booking(b3)

# Check in the first guest
hotel.check_in(b1)

# Add food or laundry charges
hotel.add_service_charge(b1, 500)

# Check out and generate invoice with 10% discount
hotel.check_out(b1, discount_percent=10)

# Make partial payments
hotel.make_payment(b1, 1000)
hotel.make_payment(b1, 850)

# Display final reports
hotel.show_available_rooms()
hotel.show_bookings()
hotel.revenue_report()
