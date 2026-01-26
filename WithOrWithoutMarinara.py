#Weather Branch

import requests

def recommend_speed(current_weather: dict) -> int:
    """
    Determine a recommended driving speed (mph)
    based on NWS weather conditions.
    """
    base_speed = 65  # normal highway speed
    desc = (current_weather.get("Condition") or "").lower()
    temp_c = current_weather.get("Temperature")
    wind = current_weather.get("Wind Speed") or 0

    # Weather condition checks
    if "thunder" in desc:
        return 25
    if "snow" in desc or "blizzard" in desc:
        return 35
    if "ice" in desc or (temp_c is not None and temp_c <= 0):
        return 30
    if "fog" in desc or "mist" in desc:
        return 40
    if "heavy rain" in desc or "downpour" in desc:
        return 45
    if "rain" in desc:
        base_speed = 55

    # Wind adjustment
    if wind > 40:       # strong crosswinds
        base_speed -= 15
    elif wind > 25:
        base_speed -= 10

    return max(base_speed, 25)


def Weather(lat: float, lon: float) -> dict:
    headers = {
        "User-Agent": "MyWeatherApp (email@example.com)"
    }

    points_url = f"https://api.weather.gov/points/{lat},{lon}"
    data_points = requests.get(points_url, headers=headers).json()["properties"]

    stations_url = data_points["observationStations"]
    stations = requests.get(stations_url, headers=headers).json()["features"]

    current_cond = {}
    if stations:
        station_id = stations[0]["properties"]["stationIdentifier"]
        obs_url = f"https://api.weather.gov/stations/{station_id}/observations/latest"
        obs = requests.get(obs_url, headers=headers).json()["properties"]

        current_cond = {
            "Temperature": obs["temperature"]["value"],  # Celsius
            "Condition": obs["textDescription"],
            "Wind Speed": obs["windSpeed"]["value"] or 0
        }

    speed = recommend_speed(current_cond)

    return {
        "current_conditions": current_cond,
        "recommended_speed_mph": speed
    }


# Example usage
if __name__ == "__main__":
    data = Weather(42.48, -85.50)
    print("Conditions:", data["current_conditions"])
    print("Recommended driving speed:", data["recommended_speed_mph"], "mph")