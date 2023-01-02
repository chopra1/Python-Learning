#1. Establish an origin and destination
#2. Calculate the distance/route
#3. Return the best route

# a very simple version that plans a trip between two popular New York tourist destinations might look like this:
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
 
print("Calculating the total distance between our points.") 
 
print("The best route is by train and will take approximately 10 minutes.") 

#without loop function
# First user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.") 
# Second user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.") 
# Third user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.") 
# Fourth user wants to travel between these two points!
print("Setting the Empire State Building as the starting point and Times Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.") 


def trip_welcome(origin, destination):
  print("Welcome to Tripcademy!")
  print("Looks like you are traveling from " + origin + "And you are heading to " + destination) 
  print("Let's get you to your destination.")
  print("Woah, look at the weather outside! Don't walk, take the train!")
  print("Looks like you're going to " + destination + " today.")
trip_welcome("Prospect Park", "Times Square") #prints: Looks like you're going to Times Square today.

# Your code below: 
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")
  print("Take lots of pictures!")
directions_to_timesSq()

# Your code below: 
print("Checking the weather for you!")

def weather_check():
  print("Looks great outside! Enjoy your trip.")
  print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")
weather_check()

# Your code below:
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)
generate_trip_instructions("Central Park")

# Write your code below: 
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print(car_rental_total + hotel_total + plane_ticket_price)
calculate_expenses(200, 100, 100, 5) #output : 1190

def calculate_taxi_price(miles_to_travel, rate, discount):
    print(miles_to_travel * rate - discount )
calculate_taxi_price(100, 10, 5) #positional arguments
calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100) #keyword arguments

# Write your code below:
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination = "Iceland", second_destination = "India", final_destination = "Germany")
trip_planner("Brooklyn", "Queens")

destination_name = "Venkatanarasimharajuvaripeta" 
# Built-in function: len()
length_of_destination = len(destination_name) 
# Built-in function: print()
print(length_of_destination) #output: 28

#help("string")

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:

# Checkpoint 1
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

# Checkpoint 2
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)

# Checkpoint 3
rounded_price = round(tshirt_price, 1)
print(rounded_price)

#variable acces outside the function
budget = 1000
  
def trip_welcome(destination="California"):
    print(" Looks like you're going to " + destination)
    print(" Your budget for this trip is " + str(budget))
 
print(budget)
trip_welcome()

favorite_locations = "Paris, Norway, Iceland"
# This function will print a hardcoded count of how many locations we have.
def print_count_locations():
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()

#Return function value
def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate
 
new_zealand_exchange = calculate_exchange_usd(100, 1.4)
 
print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 
def deduct_expense(budget, expense):
  return budget - expense

shirt_expense = 9

new_budget_after_shirt = deduct_expense( current_budget, shirt_expense )

print_remaining_budget(new_budget_after_shirt)

#Multiple return function
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']
 
def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day
monday, tuesday, wednesday = threeday_weather_report(weather_data)
 
print(monday)
print(tuesday)
print(wednesday)

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third 
  
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

# Write your code below:

def trip_planner_welcome(name): 
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome(" Chetan Chopra ")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.43)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin) #Your trip starts off in  Mumbai
  print("And you are traveling to " + destination) #And you are traveling to Delhi
  print("You will be traveling by " + mode_of_transport) #You will be traveling by Car
  print("It will take approximately " + str(estimated_time) + " hours") #It will take approximately 2 hours

destination_setup(" Mumbai ", "Delhi ", estimate, "Car")