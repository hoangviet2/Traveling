import geocoder
g = geocoder.ip('me')
# importing requests and json
import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# City Name CITY = "Hyderabad"
# API key API_KEY = "Your API Key"
# upadting the URL
URL = BASE_URL + "lat="+str(g.latlng[0])+"&lon="+str(g.latlng[1])+"&appid=dc70e182e7921fb2cdbed2815d5de5fd"
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   # name
   name = data['name']
   # sys
   sysytem = data['sys']
   print(f"Code: {sysytem['country']}")
   print(f"City: {name}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")