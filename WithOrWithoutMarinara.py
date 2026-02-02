#Gasoline

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