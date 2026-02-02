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