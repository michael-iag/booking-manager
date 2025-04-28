from behave import given, when, then
from app import BookingManager

@given('the booking manager system is initialized')
def step_impl(context):
    context.booking_manager = BookingManager()
    context.booking_ids = []

@when('I create a booking for flight "{flight_id}" with passenger "{passenger_name}" and {num_seats:d} seat')
@when('I create a booking for flight "{flight_id}" with passenger "{passenger_name}" and {num_seats:d} seats')
def step_impl(context, flight_id, passenger_name, num_seats):
    booking_id = context.booking_manager.create_booking(flight_id, passenger_name, num_seats)
    context.current_booking_id = booking_id
    if booking_id:
        context.booking_ids.append(booking_id)

@then('the booking should be created successfully')
def step_impl(context):
    assert context.current_booking_id is not None, "Booking was not created successfully"
    booking = context.booking_manager.get_booking(context.current_booking_id)
    assert booking is not None, f"Booking {context.current_booking_id} not found"

@then('the booking status should be "{status}"')
def step_impl(context, status):
    booking = context.booking_manager.get_booking(context.current_booking_id)
    assert booking["status"] == status, f"Expected status {status}, but got {booking['status']}"

@when('I retrieve the booking details')
def step_impl(context):
    context.current_booking = context.booking_manager.get_booking(context.current_booking_id)
    assert context.current_booking is not None, f"Booking {context.current_booking_id} not found"

@then('the booking should have flight ID "{flight_id}"')
def step_impl(context, flight_id):
    assert context.current_booking["flight_id"] == flight_id, \
        f"Expected flight ID {flight_id}, but got {context.current_booking['flight_id']}"

@then('the booking should have passenger name "{passenger_name}"')
def step_impl(context, passenger_name):
    assert context.current_booking["passenger_name"] == passenger_name, \
        f"Expected passenger name {passenger_name}, but got {context.current_booking['passenger_name']}"

@then('the booking should have {num_seats:d} seats')
@then('the booking should have {num_seats:d} seat')
def step_impl(context, num_seats):
    assert context.current_booking["num_seats"] == num_seats, \
        f"Expected {num_seats} seats, but got {context.current_booking['num_seats']}"

@when('I cancel the booking')
def step_impl(context):
    context.cancellation_result = context.booking_manager.cancel_booking(context.current_booking_id)

@when('I cancel the first booking')
def step_impl(context):
    if context.booking_ids:
        context.cancellation_result = context.booking_manager.cancel_booking(context.booking_ids[0])
    else:
        assert False, "No bookings to cancel"

@then('the booking should be cancelled successfully')
def step_impl(context):
    assert context.cancellation_result is True, "Booking was not cancelled successfully"

@then('the list of all bookings should contain {count:d} bookings')
def step_impl(context, count):
    all_bookings = context.booking_manager.list_bookings()
    assert len(all_bookings) == count, f"Expected {count} bookings, got {len(all_bookings)}"

@then('the list of "{status}" bookings should contain {count:d} booking')
@then('the list of "{status}" bookings should contain {count:d} bookings')
def step_impl(context, status, count):
    filtered_bookings = context.booking_manager.list_bookings(status=status)
    assert len(filtered_bookings) == count, \
        f"Expected {count} {status} bookings, got {len(filtered_bookings)}"

@then('the booking should not be created')
def step_impl(context):
    assert context.current_booking_id is None, "Booking was created when it should not have been"

@when('I create a booking for flight "" with passenger "Alice Smith" and 1 seat')
def step_impl_empty_flight_id(context):
    booking_id = context.booking_manager.create_booking("", "Alice Smith", 1)
    context.current_booking_id = booking_id
    if booking_id:
        context.booking_ids.append(booking_id)

@when('I create a booking for flight "FL001" with passenger "" and 1 seat')
def step_impl_empty_passenger_name(context):
    booking_id = context.booking_manager.create_booking("FL001", "", 1)
    context.current_booking_id = booking_id
    if booking_id:
        context.booking_ids.append(booking_id)
