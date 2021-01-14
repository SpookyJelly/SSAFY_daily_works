import random
key = 'WGNItEoVAcowu51l8P7Kt%2FrCK3JCKUVN6RaC9Td5RAoO0HJ6MkcwbpEndRPteZ2JNvZkT7vrVovr4DZPFfq19g%3D%3D'


import requests
from bs4 import BeautifulSoup

url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={key}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'
response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[5]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')

if dust > 150:
    print('매우 나쁨')
elif 150>=dust>80:
    print('나쁨')
elif 80>=dust>30:
    print('좋음')
else :
    print('아주 좋음')