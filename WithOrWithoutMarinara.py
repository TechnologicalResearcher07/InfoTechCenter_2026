<<<<<<< HEAD
#Main Branch

=======
>>>>>>> BetaTestDev
#BetaTestDev

#Welcome Branch
# Libraries Imported Here
import sys
import time

# ===== ANSI Color Codes =====
CYAN = "\033[96m"
GREEN = "\033[92m"
RESET = "\033[0m"

# ===== Welcome Messages (UNCHANGED) =====
print("\nWelcome Branch - Developer: Kiera McKimmy")
print("\nWelcome to InfotechCenter V.1.0")

# ===== Variable Initialization =====
x = 0                 # Loop counter to control boot duration
ellipsis = 0          # Controls number of dots in animation

# ===== Boot Animation Loop =====
while x != 20:
    x += 1  # Increment loop counter

    # Build boot message with animated ellipsis
    ellipsisMessage = (
        CYAN + "InfotechCenter OS Booting" + "." * ellipsis + RESET
    )

    ellipsis += 1  # Increase dots each cycle

    # Overwrite the current terminal line with updated message
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()

    # Pause to simulate boot processing
    time.sleep(.5)

    # Reset ellipsis after 3 dots
    if ellipsis == 4:
        ellipsis = 0

    # Final boot confirmation message
    if x == 20:
        print(
            GREEN
            + "\nOperating System Booted Up - Retina Scanned - Access Granted"
            + RESET
        )
    
#Weather Branch

import random  # Importing the random module to generate random weather data
from datetime import datetime, timedelta  # Importing datetime and timedelta to handle time manipulation

# Constants for Richland, MI (just for reference, though not needed for random data generation)
LATITUDE = 42.4006
LONGITUDE = -85.3305

# Step 1: Generate random weather data
def generate_random_weather():
    """
    This function generates random weather data, including the weather description,
    temperature, and wind speed.
    """
    # List of possible weather conditions
    weather_descriptions = [
        "Clear", "Partly cloudy", "Rain", "Thunderstorms", "Snow", "Fog", "Windy"
    ]
    
    # Randomly pick a weather description from the list
    weather_description = random.choice(weather_descriptions)
    
    # Random temperature between 10°F and 95°F (you can adjust these ranges as needed)
    temp = random.randint(10, 95)
    
    # Random wind speed between 0 mph and 30 mph
    wind_speed = random.randint(0, 30)
    
    # Print out the generated weather data for debugging and visibility
    print(f"Generated Weather Data: {weather_description}, Temp: {temp}°F, Wind Speed: {wind_speed} mph")
    
    # Return the weather data as a tuple
    return weather_description, temp, wind_speed

# Step 2: Determine Speed Limit Based on Weather
def get_speed_limit(weather_description, temp, wind_speed):
    """
    This function calculates the recommended speed limit based on the weather conditions,
    temperature, and wind speed.
    """
    # Default base speed limit in good weather conditions (e.g., 65 mph)
    base_speed_limit = 65
    
    # Adjust speed limit based on weather conditions
    if "snow" in weather_description.lower() or temp <= 32:
        # If snow is present or the temperature is 32°F or below, reduce speed by 20 mph
        return max(base_speed_limit - 20, 30)  # Minimum speed limit is 30 mph (don't go below that)
    elif "rain" in weather_description.lower():
        # If it's raining, reduce the speed by 15 mph
        return max(base_speed_limit - 15, 40)  # Minimum speed limit is 40 mph (don't go below that)
    elif wind_speed > 25:
        # If wind speed is greater than 25 mph, reduce the speed by 15 mph
        return max(base_speed_limit - 15, 50)  # Minimum speed limit is 50 mph (don't go below that)
    else:
        # If no severe weather conditions, maintain the base speed limit
        return base_speed_limit

# Step 3: Adjust Wake-Up Time Based on Weather
def adjust_wake_up_time(weather_description):
    """
    This function adjusts the wake-up time based on weather conditions.
    The logic assumes that bad weather requires more time for preparation.
    """
    # Default wake-up time is 6:00 AM (using a 24-hour format)
    wake_up_time = datetime.strptime('06:00', '%H:%M')

    # If the weather is bad (snow or rain), we add 30 minutes to the wake-up time
    if "snow" in weather_description.lower() or "rain" in weather_description.lower():
        wake_up_time -= timedelta(minutes=30)  # Wake up 30 minutes earlier if snow or rain is expected
    elif "fog" in weather_description.lower():
        # If there’s fog, we add 15 minutes to the wake-up time
        wake_up_time -= timedelta(minutes=15)  # Wake up 15 minutes earlier if fog is expected

    # Return the new wake-up time in a 12-hour format with AM/PM
    return wake_up_time.strftime('%I:%M %p')

# Main function to check everything
def main():
    """
    Main function that:
    1. Generates random weather data.
    2. Calculates the recommended speed limit based on weather.
    3. Adjusts the wake-up time based on the weather.
    """
    # Step 1: Generate random weather data
    weather_description, temp, wind_speed = generate_random_weather()
    
    # Step 2: Get the recommended speed limit based on the weather
    speed_limit = get_speed_limit(weather_description, temp, wind_speed)
    
    # Step 3: Adjust wake-up time based on the weather
    wake_up_time = adjust_wake_up_time(weather_description)
    
    # Print out the weather data and recommendations
    print(f"\nWeather Description: {weather_description}")
    print(f"Temperature: {temp}°F")
    print(f"Wind Speed: {wind_speed} mph")
    print(f"Recommended Speed Limit: {speed_limit} mph")
    print(f"Suggested Wake-up Time: {wake_up_time}")

# Run the main function
if __name__ == '__main__':
    main()

<<<<<<< HEAD
#Gasoline Branch
=======
#Gasoline
>>>>>>> BetaTestDev

import random

# Define car class to keep track of gas level and fuel efficiency
class Car:
    def __init__(self, current_gas_level, fuel_efficiency):
        # Current gas level in gallons
        self.current_gas_level = current_gas_level
        # Fuel efficiency in miles per gallon
        self.fuel_efficiency = fuel_efficiency

    def can_travel(self, distance):
        """
        Determine if the car can travel a certain distance with the current gas level.
        Returns True if the car can make it, False otherwise.
        """
        # Calculate maximum distance the car can travel
        max_distance = self.current_gas_level * self.fuel_efficiency
        return max_distance >= distance

    def update_gas_level(self, gas_used):
        """
        Update the car's gas level after a trip.
        """
        self.current_gas_level -= gas_used

# Define gas station class to store details of each station
class GasStation:
    def __init__(self, name, location, distance, price, is_open, has_snacks):
        self.name = name
        self.location = location
        self.distance = distance  # Distance to the gas station in miles
        self.price = price  # Price per gallon
        self.is_open = is_open  # Open or closed
        self.has_snacks = has_snacks  # Whether it has snacks/slurpies

    def get_station_details(self):
        """
        Returns a dictionary with details about the gas station.
        """
        return {
            'Name': self.name,
            'Location': self.location,
            'Distance': self.distance,
            'Price': self.price,
            'Is Open': 'Yes' if self.is_open else 'No',
            'Has Snacks/Slurpies': 'Yes' if self.has_snacks else 'No'
        }

# Create a list of gas stations with random details
def generate_gas_stations():
    stations = [
        GasStation('Speedy Gas', '123 Main St', 5, 3.50, True, True),
        GasStation('QuickFuel', '456 Elm St', 7, 3.20, False, False),
        GasStation('Fuel Express', '789 Oak St', 10, 3.00, True, True),
        GasStation('Go Gas', '101 Pine St', 4, 3.75, True, False),
        GasStation('FastFuel', '202 Maple St', 12, 2.90, True, True)
    ]
    return stations

# Main program logic
def find_nearest_station_and_check_car(car, stations):
    # Check if gas level is below 1/4 tank
    if car.current_gas_level < 0.25 * 12:  # Assuming the gas tank holds 12 gallons
        print("Gas level is below 1/4 tank. Time to find a gas station!")
        
        # Sort stations by distance (ascending)
        nearest_station = min(stations, key=lambda x: x.distance)
        
        print("Nearest gas station:", nearest_station.name)
        
        # Check if car can make it to the nearest station
        if car.can_travel(nearest_station.distance):
            print(f"You can make it to {nearest_station.name}.")
            
            # Check if the station is open
            if nearest_station.is_open:
                print(f"{nearest_station.name} is open!")
            else:
                print(f"{nearest_station.name} is closed.")
                
            # Check if station has snacks/slurpies
            if nearest_station.has_snacks:
                print(f"{nearest_station.name} has snacks/slurpies!")
            else:
                print(f"{nearest_station.name} does not have snacks/slurpies.")
            
            # Update the car's gas level after making it to the station
            print("Refueling...")
            car.update_gas_level(nearest_station.distance / car.fuel_efficiency)  # Assume 1 gallon per distance unit

            # Update phone alarm if needed
            if car.current_gas_level < 3:  # If gas level is below 3 gallons, update alarm
                print("Alarm set: You need to refuel soon.")
        else:
            print(f"You don't have enough gas to reach {nearest_station.name}.")
    else:
        print("Your gas level is above 1/4 tank, no need to refuel yet.")

# Example usage:
if __name__ == "__main__":
    # Initialize car with 2 gallons of fuel and 25 miles per gallon efficiency
    my_car = Car(current_gas_level=2, fuel_efficiency=25)

    # Generate a list of gas stations
    gas_stations = generate_gas_stations()

    # Find the nearest station and check if you can make it
    find_nearest_station_and_check_car(my_car, gas_stations)
