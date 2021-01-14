# 딕셔너리 선언
# 딕셔너리는 일반적인 순서가 없지만, 이름을 붙여서 저장할 수 있다.
my_home = {
    'location' : 'seoul',
    'area-code' : '02',

}
# 딕셔너리 원소 접근
location = my_home['location']
area_code = my_home['area-code'] # []로 가져올 때는 area-code라는 이름의 객체가 없으면 에러가 뜬다
print(location)
print(area_code)

location = my_home.get('location') 
area_code = my_home.get('area-code')
print(location)
print(area_code)
print(my_home.get('aaa')) # get()으로 가져올 때는 area-code라는 이름의 객체가 없으면 None을 반환한다.

# 딕셔너리 원소 변경
my_home['location'] = 'gwangju'
print(my_home)

my_home['area-code'] = '062'
print(my_home)