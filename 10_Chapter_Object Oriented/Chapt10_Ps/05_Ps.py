class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def get_status(self):
        print(f"Train: {self.name}, Seats Available: {self.seats}")

    def fare_info(self):
        print(f"Fare per ticket: ₹{self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket booked successfully!")
        else:
            print("No seats available!")

# Example usage
t = Train("Rajdhani Express", 2, 1500)
t.get_status()
t.book_ticket()
t.get_status()
t.fare_info()
