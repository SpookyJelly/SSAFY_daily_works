line = " 안녕하세요"

# replace 메소드는 원본을 변경하지 않는다
print(line.replace("세","시"))
print(line)


# split 메소드는 내부에 있는 것을 기분으로 쪼갠다.
# 그래서 "하"라는 글자는 없어진다.
print(line.split("하"))

#find와 index의 차이
# 둘 다 처음 등장하는 문자를 반환하지만,
# find는 없는 글자를 찾으려 하면 -1 을 반환한다.
# 하지만 index를 이용하려고 하면 밸류 에러가 뜬다.
line2 = "안녕안녕"
print(line2.index("안"))
print(line2.find("소"))


# 문자열 뒤집는 방법은 자기 문자열에서 뒤집는 방법이 있고, 새로운 빈 문자열을 만들어
# 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법이 있다.
# 자기 문자열을 이용할 경우는 swap을 위한 임시 변수가 필요하며, 반복 수행을 문자열 길이의
# 반만을 수행해야한다.

# 근데 문자열은 내부의 값을 바꿀 수 없는 immutable 한 객체이다.
# 그래서 내부의 값을 바꿀 수 있고, muttable한 객체인 리스트로 바꾸자.

# == 는 값 비교, is는 참조 비교

a = [1,2,3]
b = a
c= [1,2,3]

print(a==b)
print(b==c)
print(a is b)
print(b is c)

# 문자형 숫자를 int로 바꾸는 방법


