import json
import requests

print('Please enter your city:')
city = input()
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&appid=ba560ed47b57624171d3966bfba8e6a6' % city)
data=r.json()
print(data['weather'][0]['description'])