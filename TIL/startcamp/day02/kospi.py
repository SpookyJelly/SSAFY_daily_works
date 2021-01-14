import requests
from bs4 import BeautifulSoup

KOSPI_URL = 'https://finance.naver.com/sise/' # 대문자로 표현 ==> 상수 --> 잘 안 변하는 값이라는 걸 알려주는 것.
hwan_URL = 'https://finance.naver.com/marketindex/'

#1.응답으로 뭔가 오는데, 거기서 HTML 문서만 보여줘
response = requests.get(KOSPI_URL).text
response2 = requests.get(hwan_URL).text
# 2. 문서(HTML)를 파이썬이 이해하기 좋게끔 구조화 시켜줘
soup = BeautifulSoup(response,'html.parser')
soup2 = BeautifulSoup(response2,'html.parser')
#3. 구조화된 문서에서 내가 원하는 정보를 가져와줘
kospi = soup.select_one('#KOSPI_now')

#3.1 환율까지 알아보자
hwan = soup2.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

# 4. 이 정보에서 text 꼴만 가져와줘 (태그 <> 제외)
print('현재 코스피 지수는 {0}입니다.'.format(kospi.text))

# 4.1 환율 출력
# 처음에 이게 None으로 나온 이유가, 환율 셀렉터를 가져오는 URL 주소와
# 그것을 구조화 시키지 않았기 때문이다.
# 그래서 다시 처음부터 URL 추가하고, 새로운 변수들을 만들어서 정보를 가져왔다.
print(f'현재 환율은 {hwan.text}입니다.') 
