# Feature: Booking Manager Functionality
# This feature covers the core functionality of managing flight bookings.

Feature: Booking Management
  As a travel agent,
  I want to manage flight bookings
  So that I can serve my customers efficiently.

  @sanity @critical
  Scenario: Create a new booking
    Given the booking manager system is initialized
    When I create a booking for flight "FL001" with passenger "Alice Smith" and 1 seat
    Then the booking should be created successfully
    And the booking status should be "CONFIRMED"

  @sanity
  Scenario: Retrieve booking details
    Given the booking manager system is initialized
    When I create a booking for flight "FL002" with passenger "Bob Johnson" and 2 seats
    And I retrieve the booking details
    Then the booking should have flight ID "FL002"
    And the booking should have passenger name "Bob Johnson"
    And the booking should have 2 seats

  @critical
  Scenario: Cancel a booking
    Given the booking manager system is initialized
    When I create a booking for flight "FL003" with passenger "Charlie Brown" and 3 seats
    And I cancel the booking
    Then the booking should be cancelled successfully
    And the booking status should be "CANCELLED"

  @sanity
  Scenario: List all bookings
    Given the booking manager system is initialized
    When I create a booking for flight "FL001" with passenger "Alice Smith" and 1 seat
    And I create a booking for flight "FL002" with passenger "Bob Johnson" and 2 seats
    Then the list of all bookings should contain 2 bookings

  @edgecase
  Scenario: List bookings by status
    Given the booking manager system is initialized
    When I create a booking for flight "FL001" with passenger "Alice Smith" and 1 seat
    And I create a booking for flight "FL002" with passenger "Bob Johnson" and 2 seats
    And I cancel the first booking
    Then the list of "CONFIRMED" bookings should contain 1 booking
    And the list of "CANCELLED" bookings should contain 1 booking

  @negative
  Scenario: Create booking with invalid inputs
    Given the booking manager system is initialized
    When I create a booking for flight "" with passenger "Alice Smith" and 1 seat
    Then the booking should not be created
    When I create a booking for flight "FL001" with passenger "" and 1 seat
    Then the booking should not be created
    When I create a booking for flight "FL001" with passenger "Alice Smith" and 0 seats
    Then the booking should not be created
