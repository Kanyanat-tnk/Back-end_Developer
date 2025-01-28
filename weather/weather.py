import requests
API_key = '911a1909a17862c33b94d112f18443fd'
city = 'bangkok'

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
#https://api.openweathermap.org/data/2.5/weather?q=bangkok&appid=911a1909a17862c33b94d112f18443fd
result = requests.get(url).json()
#print(result)

city_name = result['name']
country = result['sys']['country']
weather = result['weather'][0]['main']
description = result['weather'][0]['description']
temp = result['main']['temp'] -273.15



print(f'เมือง {city_name} ประเทศ {country}')
print(f'สภาพอากาศ {weather} มีลักษณะ {description}')
print(f'อุณหภูมิ {temp:.2f} C')