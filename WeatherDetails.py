import requests
from pprint import pprint  #for beautiful format

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=d618e6a2152090eb329548bd5320b178&units=metric'.format(city)

res = requests.get(url)

data = res.json()

#print(res)

#pprint(data)

temp = data['main']['temp']
wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

pressure = data['main']['pressure']
humidity = data['main']['humidity']

description = data['weather'][0]['description']

print('Temperature :{} degree celcius'.format(temp))
print('Wind Speed : {} m/s'.format(wind_speed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('Pressure : {}'.format(pressure))
print('Humidity : {}'.format(humidity))
print('Description : {}'.format(description))
      
      
