import requests
import os

TOKEN = os.getenv('TOKEN')
CITY =  os.getenv('CITY')
SUCCESS_CODE = 200

try:
    request = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + CITY + '&appid=' + TOKEN)
    if request.status_code == SUCCESS_CODE:
        json_out = request.json()
        print('source = openweathermap, city = "' + CITY +
            '", description = "' + json_out["weather"][0]["description"] +
            '", temp = "' + str(json_out["main"]["temp"]) + '", humidity = "' + str(json_out["main"]["humidity"]) + '"')
    else:
        print("Not possible to get data or reach weather web-site")
except:
    print("Something goes wrong or remote site is not accessable!")
