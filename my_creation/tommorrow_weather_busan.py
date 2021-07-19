import requests
from pprint import pprint

url ='https://www.metaweather.com/api/'
location = 1132447 #부산
response = requests.get(f'{url}location/{location}/').json()

# pprint(response)
tommorrow_weather = response['consolidated_weather'][1]['weather_state_name']
tommorrow_max_temp = response['consolidated_weather'][1]['max_temp']
tommorrow_min_temp = response['consolidated_weather'][1]['min_temp']

print(f"""내일 부산의 날씨는 {tommorrow_weather}입니다.
내일의 최고기온 : {tommorrow_max_temp}℃
내일의 최저기올 : {tommorrow_min_temp}℃ """)



