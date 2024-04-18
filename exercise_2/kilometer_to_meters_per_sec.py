"""
Write a program that reads a value in kilometers per hour
form the console and displays it in meters per second . 
The general formula for the conversation is as follows:
1 km / 1h = 1000 m / 3600 s

"""

speed_km = int(input("Enter speed in km/h: "))
meter_per_sec = (speed_km * 1000)/ 3600

print(f"{speed_km} km/h is equal to {meter_per_sec} m/s")