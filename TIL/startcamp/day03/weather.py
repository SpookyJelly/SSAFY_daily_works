import requests

#ex) /api/location/search/?query=london
URL = 'https://www.metaweather.com/api/location/search/?query=seoul'

# URL을 통해서 던져주는 파일형식이 json 인지 xml인지 어떻게 아는가??
# 그건 대부분 API 설명 탭에서 알려준다.
response = requests.get(URL).json()
print(response)

# 리스트 안에 딕셔너리 있는 자료 꼴이 아직 익숙하지가 않다.
# 계속 연습해라.
woeid = response[0].get('woeid')
#[{'title': 'Seoul', 'location_type': 'City', 'woeid': 1132599, 'latt_long': '37.557121,126.977379'}]


# 미니 과제
# 1. 요청 보낸다.
# 2. 응답 저장 후 json을 딕셔너리로 변환
# 3. 딕셔너리에서 최고 기온 & 최저 기온 가져온다.
# 4. 출력!

# metaweather API (서울)
URL_seoul = f'https://www.metaweather.com/api/location/{woeid}/'

# 서울의 날씨 정보를 metaweather URL을 통해서 json 파일로 받아와서 저장한 변수
response_seoul = requests.get(URL_seoul).json()


min_temp_seoul = response_seoul.get('consolidated_weather')[0].get('min_temp')
max_temp_seoul = response_seoul.get('consolidated_weather')[0].get('max_temp')
applicable_date_seoul = response_seoul.get('consolidated_weather')[0].get('applicable_date')
print(f'서울의 {applicable_date_seoul} 최저기온 {min_temp_seoul}, 최고 기온{max_temp_seoul} 입니다.')

