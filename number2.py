import requests
city='Moscow,RU'
appid='94e1e74064dac13fbb8e787f50f6bc0a'
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print('Скорость ветра', data['wind']['speed'], "м/с")
print('Видимость', data['visibility'], 'км')

print('__________________________________________________________________________________')

res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], ">",
          "Температура <", '{0:+3.0f}'.format(i['main']['temp']), ">\r\n",
          "Погодные условия <", i['weather'][0]['description'], ">\r\n",
          "Скорость ветра <", i['wind']['speed'], 'м/с', '>\r\n',
          "Видимость", i['visibility'], "км")
    print("_______________________________________________________")