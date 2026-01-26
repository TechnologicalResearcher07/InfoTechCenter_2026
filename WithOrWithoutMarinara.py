#Weather Branch

import random

def weather ():
    conditions = [
        "Sunny",
        "Cloudy",
        "Stormy",
        "Snowy",
        "Rainy",
        "Windy",
        "Foggy"
    ]
    return random.choice(conditions)

print("Today the weather is", weather()+".")