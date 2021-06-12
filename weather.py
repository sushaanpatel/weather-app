#Created by Sushaan Patel
import os
import dotenv
import requests, json
from tkinter import *

root = Tk()
root.title("Simple Weather")

dotenv.load_dotenv()
api_key = os.environ.get('API_KEY')

def main():
    location = str(input("Enter City Name : ")).lower()
    info = {'q' : location, "appid" : api_key, "units" : "metric"}
    r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?", params=info)
    weather = r.json()
    if weather["cod"] == '404':
        pass
        # print("\nCity not found")
    else:
        pass
        # print("\n-----------")
        # print("   Basic   ")
        # print("-----------")
        # print("Temperature : " + str(round(weather["main"]["temp"])) + u"\N{DEGREE SIGN}C")
        # print("Feels Like : " + str(round(weather["main"]["feels_like"])) + u"\N{DEGREE SIGN}C")
        # print("Pressure : " + str(round(weather["main"]["pressure"])) +  "mBar")
        # print("Humidity : " + str(round(weather["main"]["humidity"])) + "%")
        # print("-------------")
        # print("Wind & Clouds")
        # print("-------------")
        # print("Clouds : " + weather["weather"][0]["description"])
        # print("Wind Speed : " + str(round(weather["wind"]["speed"] * 3.6, 2)) + " km/h")
        # print("Wind Direction : " + str(weather["wind"]["deg"]) + u"\N{DEGREE SIGN} from N")

main()