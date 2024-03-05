# 함수 사용
import requests
import json 

# 함수 선언
def main(city, apikey='720d7f9e604a5f0785728eca2145f223', lang='kr'):
     api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric'
     response = requests.get(api)

     if response.status_code == 200:
         data = json.loads(response.text)
         weather = data['weather'][0]['main']
         temp = data['main']['temp']
         return weather, temp
     else:
         print('요청 실패')

if __name__ == "__main__":
     print(main.__name__)
     city = "Seoul"
     weather, temp = main(city)
     print(weather, temp)
