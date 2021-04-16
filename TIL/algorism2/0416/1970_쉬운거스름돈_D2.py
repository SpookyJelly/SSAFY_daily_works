# 접근방법 (수정)
# 0. 생각해보니 너무 비효율적임. 타자를 너무 쳐야함
# 1. if문을 함수형으로 바꿔서 코드 내에서 반복문은 하나만 등장하게 함
# 2. 원화 단위와 사용매수를 편하게 카운트하기 위해서 딕셔너리 자료형 사용
# 3. 양식에 맞게 return
import sys
sys.stdin = open('1970_input.txt','r')

# 입력 : 남은 돈, 이번에 쓰는 지폐
def test(money,jipae):
    cnt =0
    # jipae가 string 꼴로 들어가므로, int로 전환해서 계산한다
    while((money>=int(jipae))):
        money -= int(jipae)
        cnt += 1
    #반환 : 이번 지폐 쓴 횟수, 남은 돈
    return [cnt, money]

T = int(input())

for t in range(T):
    money = int(input())
    
    money_dic ={
        
        '50000' : 0,
        '10000' : 0,
        '5000' : 0,
        '1000' : 0,
        '500' : 0,
        '100' : 0,
        '50' : 0,
        '10' : 0,
        }
    
    while (money>0):
        #input값이 10원 단위 밑으로 들어오는 경우도 있음,
        # 근데 내가 설계한 구조에서는 money가 10원 미만이면 무한 루프를 도니까, 강제 탈출 조건 걸어둠
        if money<10: 
            break
        # money_dic,keys() --> ['50000','10000'....]
        # for문 돌 때마다 test 함수에 다른 원화 단위가 들어감
        # money 변수도 test 함수 돌고 나오면 항상 바뀐다
        for i in list(money_dic.keys()):
            cnt, money = test(money,i)
            money_dic[i] = cnt
    #1. money_dic의 value를 list형으로 변환 (요소 = int꼴)
    #2. 이후 .join 메서드를 쓰기 위해 map 함수로 str함수를 적용해줌
    #3. 그 결과를 result라는 변수에 할당
    result = list(map(str,list(money_dic.values())))
    print('#{0}\n{1}'.format(t+1,' '.join(result)))