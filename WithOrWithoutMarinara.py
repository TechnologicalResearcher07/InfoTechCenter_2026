#Weather Branch

import requests
from datetime import datetime, timedelta

# Function to get weather data from the National Weather Service API
def get_weather_data(latitude, longitude):
    url = f"https://api.weather.gov/points/{latitude},{longitude}/forecast"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast = data['properties']['periods'][0]  # Get the first forecast period
        return forecast['shortForecast'], forecast['temperature'], forecast['temperatureUnit']
    else:
        print("Error fetching weather data.")
        return None, None, None

# Function to determine the recommended driving speed
def get_driving_speed(weather):
    weather = weather.lower()
    
    if "clear" in weather or "sunny" in weather:
        return 65  # Clear weather, normal speed
    elif "rain" in weather or "snow" in weather:
        return 50  # Moderate conditions, slow down
    elif "fog" in weather or "heavy" in weather:
        return 35  # Poor visibility or icy roads
    else:
        return 65  # Default speed if conditions are not severe

# Function to calculate how many minutes earlier you need to wake up
def calculate_wake_up_time(current_speed, road_speed=65, drive_time=30):
    speed_factor = road_speed / current_speed  # Adjust wake-up time based on speed
    additional_time = int((speed_factor - 1) * drive_time)  # Calculate how much extra time is needed
    return additional_time

# Main program logic
def weather_alert(latitude, longitude):
    # Get weather information
    weather, temperature, temp_unit = get_weather_data(latitude, longitude)
    
    if weather:
        print(f"Current weather: {weather}, Temperature: {temperature} {temp_unit}")
        
        # Get the recommended driving speed based on weather
        driving_speed = get_driving_speed(weather)
        print(f"Recommended driving speed: {driving_speed} mph")
        
        # Calculate how many minutes earlier to wake up
        wake_up_adjustment = calculate_wake_up_time(driving_speed)
        print(f"Wake up {wake_up_adjustment} minutes earlier for safer driving conditions.")
        
        # Calculate the new alarm time
        current_alarm_time = datetime.strptime('09:00 AM', '%I:%M %p')
        new_alarm_time = current_alarm_time - timedelta(minutes=wake_up_adjustment)
        
        print(f"Set your alarm to: {new_alarm_time.strftime('%I:%M %p')}")
        
        # Send a message (simulating sending a message to your phone)
        alert_message = f"Weather Alert: Due to {weather}, wake up {wake_up_adjustment} minutes earlier. Set your alarm for {new_alarm_time.strftime('%I:%M %p')}"
        return alert_message
    else:
        return "Error: Could not fetch weather data."

# Example usage (replace latitude and longitude with your location's coordinates)
latitude = 37.7749  # Example: San Francisco's latitude
longitude = -122.4194  # Example: San Francisco's longitude

alert_message = weather_alert(latitude, longitude)
print(alert_message)
