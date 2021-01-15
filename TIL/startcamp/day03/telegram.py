# 목표 기능
# 파이썬 코드를 통해 주기적으로 챗봇에게 미세먼지 정보전달

# 1. 매일 특정 시점에, 파이썬 코드로 미세먼지 정보를 가져온다.
# 2. 가져온 미세먼지 정보를 텔레그램 서버로 전달한다.
# 3. 텔레그램 서버가 우리 텔레그램 채팅방으로 메세지를 전달한다.
import requests
import random

token = '1540584588:AAEsSL3OJ03pEJFc2l-oSLDP8qWyq89_nU4'
url = f'https://api.telegram.org/bot{token}/getUpdates'
print(url)
response = requests.get(url).json() 
# 이렇게하면 response 안에 딕셔너리가 있다,

chat_id = response.get('result')[0].get('message').get('from').get('id')
# 미니 과제 :chat_id를 꺼내보세요
# 미니 과제 2) 로또 번호 6개를 추천해서 보내주세요

#lotto_list = range(1,46)
#lotto = sorted(random.sample(lotto_list,6))
#lotto2=', '.join(map(str,lotto))

# =====================================================
# 파파고 번역 요청 코드
""" naver_client_id = 'KG6q4rQZTKxIRcBcOIbH'
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
 """
#===============================================

# 미세먼지 정보 가져오는 코드


key = 'nX0Jhv9BOoYnadc73VtQqK%2BznofRLKN7LMwpOeThFb6dPKn0AflRPhLHGc3sAHphzXx6rP%2FDtxOe40UsXgEYqw%3D%3D'
return_type = 'json'
rows = 100
page_no = 1
sido_name = '서울'
version = '1.0'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows={rows}&pageNo={page_no}&returnType={return_type}&sidoName={sido_name}&ver={version}'
response = requests.get(url).json() #json 파일로 받아온다

gwangjin = response.get('response').get('body').get('items')[0].get('stationName')
gwangjin_dust = response.get('response').get('body').get('items')[0].get('pm10Value')

text = f'{gwangjin}의 미세먼지는 {gwangjin_dust} 입니다.'


# ==============================================


#text = f'{data["text"]} 문장의 번역 결과는 {translatedText}입니다.'

message_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url) 


# 여기는 왜 변수에 저장도 안하고, .json()을 쓰지도 않았는데, 작동을 할까?
# 작동이라고 말하기도 애매한게, 얘는 그냥 내 요청을 수행했을 뿐이다.
# 내 명령을 서버에 전송하기만 해서 이다.


