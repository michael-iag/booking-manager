"""
Booking Manager API - A simple Python application for managing flight bookings
"""

class BookingManager:
    def __init__(self):
        # In-memory storage for bookings
        self.bookings = {}
        self.next_booking_id = 1

    def create_booking(self, flight_id, passenger_name, num_seats):
        """
        Creates a new booking for a given flight.

        Args:
            flight_id (str): The ID of the flight to book.
            passenger_name (str): The name of the passenger.
            num_seats (int): The number of seats to book.

        Returns:
            int: The ID of the newly created booking, or None if booking failed.
        """
        if not flight_id or not passenger_name or num_seats <= 0:
            return None # Invalid input

        # In a real app, you would check flight availability here
        # For simplicity, we assume the flight exists and has seats

        booking_id = self.next_booking_id
        self.bookings[booking_id] = {
            "id": booking_id,
            "flight_id": flight_id,
            "passenger_name": passenger_name,
            "num_seats": num_seats,
            "status": "CONFIRMED"
        }
        self.next_booking_id += 1
        return booking_id

    def get_booking(self, booking_id):
        """
        Retrieves the details of a specific booking.

        Args:
            booking_id (int): The ID of the booking to retrieve.

        Returns:
            dict: The booking details if found, otherwise None.
        """
        return self.bookings.get(booking_id)

    def cancel_booking(self, booking_id):
        """
        Cancels an existing booking.

        Args:
            booking_id (int): The ID of the booking to cancel.

        Returns:
            bool: True if the booking was successfully cancelled, False otherwise.
        """
        booking = self.get_booking(booking_id)
        if booking and booking["status"] == "CONFIRMED":
            booking["status"] = "CANCELLED"
            # In a real app, you might release the seats here
            return True
        return False

    def list_bookings(self, status=None):
        """
        Lists all bookings, optionally filtering by status.

        Args:
            status (str, optional): Filter bookings by status (e.g., "CONFIRMED", "CANCELLED"). Defaults to None (all bookings).

        Returns:
            list: A list of booking dictionaries.
        """
        if status:
            return [b for b in self.bookings.values() if b["status"] == status]
        else:
            return list(self.bookings.values())

# Example usage
if __name__ == "__main__":
    manager = BookingManager()

    # Create bookings
    booking1_id = manager.create_booking("FL001", "Alice Smith", 1)
    booking2_id = manager.create_booking("FL003", "Bob Johnson", 2)
    print(f"Created booking {booking1_id} for Alice Smith.")
    print(f"Created booking {booking2_id} for Bob Johnson.")

    # Get booking details
    booking1 = manager.get_booking(booking1_id)
    print(f"\nBooking {booking1_id} details: {booking1}")

    # List bookings
    all_bookings = manager.list_bookings()
    print(f"\nAll bookings ({len(all_bookings)}): {all_bookings}")

    # Cancel a booking
    cancelled = manager.cancel_booking(booking1_id)
    print(f"\nCancelled booking {booking1_id}: {cancelled}")

    # List confirmed bookings
    confirmed_bookings = manager.list_bookings(status="CONFIRMED")
    print(f"\nConfirmed bookings ({len(confirmed_bookings)}): {confirmed_bookings}")

    # List cancelled bookings
    cancelled_bookings = manager.list_bookings(status="CANCELLED")
    print(f"\nCancelled bookings ({len(cancelled_bookings)}): {cancelled_bookings}")
