# This program offers holiday options to the user, retrieves their choices
# and returns the overall cost and cost breakdown.

# Program can be restarted at the end upon user choice.

import os
import sys

# Backend inputs
option_1_city_name = "Malta"
option_1_flight_cost = 100
option_1_hotel_name = "Le Margherite"
option_1_hotel_cost = 30
option_1_car_type = "Car"
option_1_car_cost = 18

option_2_city_name = "Reykjavik"
option_2_flight_cost = 399
option_2_hotel_name = "Blue House B&B"
option_2_hotel_cost = 80
option_2_car_type = "4x4"
option_2_car_cost = 100

option_3_city_name = "Vancouver"
option_3_flight_cost = 649
option_3_hotel_name = "Barclay Hotel"
option_3_hotel_cost = 100
option_3_car_type = "SUV"
option_3_car_cost = 50


# Restart program upon user choice
def restart_program():
    """
    This function restarts the program upon user choice
    """
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Define hotel_cost
# return num_nights * cost per night
def hotel_cost() -> float:
    """
    Ascertains correct hotel cost based on user input
    Multiplies hotel cost per night by user-input number of nights and
    returns the result
    """
    if city_flight == 1:
        return option_1_hotel_cost * num_nights
    elif city_flight == 2:
        return option_2_hotel_cost * num_nights
    else:
        return option_3_hotel_cost * num_nights

# Define plane_cost
# return cost as per user choice
def plane_cost() -> float:
    """
    Ascertains correct flight cost based on user input and returns the result
    """
    if city_flight == 1:
        return option_1_flight_cost
    elif city_flight == 2:
        return option_2_flight_cost
    else:
        return option_3_flight_cost

# Define car_rental
# return rental_days * cost per day
def car_rental() -> float:
    """
    Ascertains relevant car rental cost based on user input
    Multiplies rental cost per day by user-input number of days and
    returns the result
    """
    if city_flight == 1:
        return option_1_car_cost * rental_days
    elif city_flight == 2:
        return option_2_car_cost * rental_days
    else:
        return option_3_car_cost * rental_days

# Define holiday_cost
# return hotel_cost + place_cost + car_rental
def holiday_cost() -> float:
    """
    Calls up hotel_cost, place_cost and car_rental
    Calculates and returns total cost of the holiday booking
    """
    return hotel_cost() + plane_cost() + car_rental()


print(
    "\n<<< Welcome to the davemakebeer holiday corporation's holiday cost "
    "calculator >>>"
)

print(
    "\nWe're currently offering holidays to these three delightful "
    "destinations:"
)

# Display user options
print("\n\t\t\tFlights\t\tHotel\t\tCar Rental\n"

    f"1. {option_1_city_name}\t\t£{option_1_flight_cost}\t\t"
    f"£{option_1_hotel_cost}\t\t£{option_1_car_cost}\n"

    f"2. {option_2_city_name}\t\t£{option_2_flight_cost}\t\t"
    f"£{option_2_hotel_cost}\t\t£{option_2_car_cost}\n"

    f"3. {option_3_city_name}\t\t£{option_3_flight_cost}\t\t"
    f"£{option_3_hotel_cost}\t\t£{option_3_car_cost}\n"
)

# Retrieve user input for chosen flight destination
while True:
    city_flight = input(
        "Where would you like to travel to? Enter 1, 2 or 3:\t"
    )
    try:        # error handling to ensure valid input
        city_flight = int(city_flight)
        if city_flight > 3:
            print("I'm sorry, we currently only offer 3 options.")
        else:
            break
    except ValueError:
        print("I didn't catch that. Please try again.")

# Retrieve user input for number of nights in hotel
while True:
    num_nights = input("How many nights will you be staying?\t\t\t")
    try:        # error handling to ensure valid input
        num_nights = int(num_nights)
        break
    except ValueError:
        print("I didn't catch that. Please enter a whole number.")

# Retrieve user input for number of car rental days
while True:
    rental_days = input("How many days would you like to rent a car for?\t\t")
    try:        # error handling to ensure valid input
        rental_days = int(rental_days)
        if rental_days > num_nights + 1: # ensure car rental <= hotel stay
            print(
                "I'm afraid you can only rent a car as long as you are "
                "staying at the hotel."
            )
        else:
            break
    except ValueError:
        print("I didn't catch that. Please try again.")

# Assign destination details as per user choice
if city_flight == 1:
    destination_city = option_1_city_name
    hotel_name = option_1_hotel_name
    car_type = option_1_car_type
elif city_flight == 2:
    destination_city = option_2_city_name
    hotel_name = option_2_hotel_name
    car_type = option_2_car_type
else:
    destination_city = option_3_city_name
    hotel_name = option_3_hotel_name
    car_type = option_3_car_type

cost_of_hotel = hotel_cost()
cost_of_flight = plane_cost()
cost_of_car = car_rental()
cost_of_holiday = holiday_cost()

print(
    "\n<<< The davemakebeer holiday corporation is thrilled to quote this "
    "holiday for you >>>\n"
)

# Output price breakdown
print(
    f"Return flights to {destination_city}:\t\t£{cost_of_flight}\n"
    f"{num_nights} nights in {hotel_name}:\t\t£{cost_of_hotel}\n"
    f"{car_type} rental for {rental_days} days:\t\t\t£{cost_of_car}\n"
    f"Total cost of booking:\t\t\t£{cost_of_holiday}\n"
)

# Retrieve user choice of proceed to payment (end this program) or restart
if __name__ == '__main__':
    while True:
        proceed_or_restart = input(
            "Would you like to proceed to payment or choose another "
            "holiday?\nType 'proceed' or 'restart':\t\t"
        ).lower()
        if proceed_or_restart == "proceed":
            print("\nPayment system under development. See you again soon.")
            break
        elif proceed_or_restart == "restart":
            restart_program()
        else:
            print("I didn't catch that. Please try again.")
