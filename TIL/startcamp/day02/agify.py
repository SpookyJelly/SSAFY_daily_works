import requests

name = 'eric'
API_URL = f'https://api.agify.io/?name={name}' 
#API는 어떤 사이트에 요청을 보내는것?
# 크롤링은 어떤 사이트에 요청한 정보를 긁어오는 것?
response = requests.get(API_URL).json() #URL에서 json 파일을 불러온다,
print(response)
print(type(response)) # 웹에서는 json파일이지만, 파이썬에서 실행하면 dictionary 형태가 된다.

#미니 과제
# oo의 나이는 oo입니다. 라고 출력해주세요!
name = response.get('name')
age = response.get('age')
print(f'{name}의 나이는 {age}입니다.')