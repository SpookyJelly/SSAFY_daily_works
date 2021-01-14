# 미니 실습
# 1. 어제 먹은 음식들로 채워진 리스트를 만들어보시오.
meal_yesterday = ['프렌치 토스트','비빔국수', '햄버거']
# 2. 첫번째 음식을 출력하시오.
print(meal_yesterday[0])
# 3. 두번째 음식을 초밥으로 바꾸시오.
meal_yesterday[1] = '초밥'
print(meal_yesterday)
print(meal_yesterday[0], end = ',')
print(meal_yesterday[1], end = ',')
print(meal_yesterday[2], end = '\n')

print(','.join(meal_yesterday))