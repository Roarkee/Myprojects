
import requests
from dotenv import load_dotenv
import os
from datetime import timezone, datetime
load_dotenv()
API_KEY=os.getenv("API_KEY")
BASE_URL="https://api.openweathermap.org/data/2.5/weather?"

def WeatherApp(city):
    url=BASE_URL+"appid="+ API_KEY +"&q="+city
    response=requests.get(url).json()
    weather=response["weather"][0]["description"]
    temperature=response["main"]["temp"]-275.15    
    humidity=response["main"]["humidity"]
    pressure=response["main"]["pressure"]
    sunrise_time=datetime.fromtimestamp(response["sys"]["sunrise"]+response["timezone"], timezone.utc).isoformat()
    sunset_time=datetime.fromtimestamp(response["sys"]["sunset"]+response["timezone"], timezone.utc).isoformat()
    return weather,temperature,humidity,pressure, sunrise_time, sunset_time