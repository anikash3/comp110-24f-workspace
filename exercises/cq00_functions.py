weather = input("Whats the weather like?")

def get_weather_report() -> None:   
    if weather == "cold" or weather =="rainy":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I dont recognize this weather")


get_weather_report()
