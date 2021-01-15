import requests
from pprint import pprint # 자주 쓰는 함수는 아닌데 특수하게 씀

key = 'nX0Jhv9BOoYnadc73VtQqK%2BznofRLKN7LMwpOeThFb6dPKn0AflRPhLHGc3sAHphzXx6rP%2FDtxOe40UsXgEYqw%3D%3D'
return_type = 'json'
rows = 100
page_no = 1
sido_name = '서울'
version = '1.0'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows={rows}&pageNo={page_no}&returnType={return_type}&sidoName={sido_name}&ver={version}'
response = requests.get(url).json() #json 파일로 받아온다
#print(response)
#pprint(response) # 출력할때 조금 이쁘게 주는 형태

# 미니 과제 )
# 'sidoName의 미세먼지는 pm10valu입니다.'라는 메세지를 출력해주세요

# 나는 처음에 None으로 나왔던 이유가 처음 중괄호를 고려하지 않았다.
# respone라는 변수에 들어가면 딕셔너리 내에 response라는 새로운 딕셔너리가 있다.
# 근데 나는 파이썬 변수 response == json 키값 response와 같은걸로 봤다
# 이름이 같아서 헷갈린 것이다. 
gwangjin = response.get('response').get('body').get('items')[0].get('stationName')
gwangjin_dust = response.get('response').get('body').get('items')[0].get('pm10Value')



print(f'{gwangjin}의 미세먼지는 {gwangjin_dust} 입니다.')