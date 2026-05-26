# from ast import main

# import requests

# def get_weather(city):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c4b10a6b70933c2da8765230665464a5"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an error for HTTP errors
#         data= response.json()        
#         for key,value in data['main'].items():
#             print(f"{key.capitalize()}: {value}")
#     except requests.RequestException as e:
#         print(e)

# city=input("Enter city name: ")
# get_weather(city)

#Watsapp msg
import pywhatkit

phone_number = input("Enter the phone number (with country code): ")
message = input("Enter the message you want to send: ")
pywhatkit.sendwhatmsg(phone_number, message, 10, 53)