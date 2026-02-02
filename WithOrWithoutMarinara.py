#Weather Branch

import random
from datetime import datetime, timedelta

# Constants for Richland, MI (just for reference)
LATITUDE = 42.4006
LONGITUDE = -85.3305

# Step 1: Generate random weather data
def generate_random_weather():
    weather_descriptions = [
        "Clear", "Partly cloudy", "Rain", "Thunderstorms", "Snow", "Fog", "Windy"
    ]
    
    # Randomly pick a weather description
    weather_description = random.choice(weather_descriptions)
    
    # Random temperature between 10°F and 95°F (for example)
    temp = random.randint(10, 95)
    
    # Random wind speed between 0 mph and 30 mph
    wind_speed = random.randint(0, 30)
    
    print(f"Generated Weather Data: {weather_description}, Temp: {temp}°F, Wind Speed: {wind_speed} mph")
    
    return weather_description, temp, wind_speed

# Step 2: Determine Speed Limit Based on Weather
def get_speed_limit(weather_description, temp, wind_speed):
    base_speed_limit = 65  # Example base speed limit in good conditions
    
    # Adjust speed based on weather conditions
    if "snow" in weather_description.lower() or temp <= 32:
        return max(base_speed_limit - 20, 30)  # Slow down in snow or freezing temperatures (min speed 30 mph)
    elif "rain" in weather_description.lower():
        return max(base_speed_limit - 15, 40)  # Slow down in rain (min speed 40 mph)
    elif wind_speed > 25:
        return max(base_speed_limit - 15, 50)  # Slow down in high winds (min speed 50 mph)
    else:
        return base_speed_limit  # Normal speed limit for clear weather

# Step 3: Adjust Wake-Up Time Based on Weather
def adjust_wake_up_time(weather_description):
    # Default wake-up time is 6:00 AM
    wake_up_time = datetime.strptime('06:00', '%H:%M')

    # Add extra time if weather is bad
    if "snow" in weather_description.lower() or "rain" in weather_description.lower():
        wake_up_time -= timedelta(minutes=30)  # Add 30 mins if snow or rain is expected
    elif "fog" in weather_description.lower():
        wake_up_time -= timedelta(minutes=15)  # Add 15 mins if fog is expected

    return wake_up_time.strftime('%I:%M %p')

# Main function to check everything
def main():
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
