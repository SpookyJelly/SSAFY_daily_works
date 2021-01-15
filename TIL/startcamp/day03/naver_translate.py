import requests
from pprint import pprint

naver_client_id = 'KG6q4rQZTKxIRcBcOIbH'
naver_client_secret = 'quFMjEvmey'

papago_url = 'https://openapi.naver.com/v1/papago/n2mt'


# 요청을 보내는 3가지 방식 : get(가져와줘), post(처리해줘), put
'''
get 은 URL에 정보를 담아서 보내지만
post는 body에 정보를 숨겨서 보낸다.
'''
data ={
    'source' : 'ko',
    'target' : 'en',
    'text' : '최고의 웹 개발자가 될꺼야.',
}

headers = {
    'X-Naver-Client-Id':naver_client_id,
    'X-Naver-Client-Secret' :naver_client_secret,
}

response = requests.post(papago_url,data=data,headers=headers).json()

translatedText = response.get('message').get('result').get('translatedText')
print(translatedText)