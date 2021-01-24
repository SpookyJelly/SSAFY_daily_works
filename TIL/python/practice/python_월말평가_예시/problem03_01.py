import json
# 접근 방안
# 1. temperatures 리스트에 접근. maximum 리스트, minimum 리스트 생성 
# 2. temperatures[i][0] 을 추려서, 새로운 리스트로 만듬 --> 최고 기온
# 3. temperatures[i][1] 을 추려서, 새로운 리스트로 만듬 --> 최저 기온
# 4. 'maximum' : 최고기온 , 'minimum' : 최저기온 꼴의 사전자료형 만듬
# 5. 4를 반환

def turn(temperatures):
    maximum = []
    minimum = []
    for temperature in temperatures: #temperature == [9, -3] ...
        maximum += temperature[0:1] 
        minimum += temperature[1:2]

    '''
    리스트의 연결을 사용하려면, 이어붙이려는 대상도 시퀀스형 자료여야한다.
    아래와 같은 코드라면 오류가 나는데,
    
    maximum += temperature[0]
    minimum += temperature[1]

    왜냐하면 temperature[0] / [1] 은 int형 자료이기 때문이다.
    int는 iterable(반복가능한) 객체가 아니기 때문에 합 연산이 안된다.
    
    그렇기 때문에 리스트 슬라이싱을 이용해서, 리스트 꼴로 더하기를 반복한 것이다.
    
    '''


    '''
    다른 방식 (.append()를 활용)

    maximum = []
    minimum = []
    for temperature in temperatures:
        maximum.append(temperature[0])
        minimum.append(temperatrue[1])
    
    '''

    temperature_dic = {

        'maximum' : maximum,
        'minimum' : minimum

    }
    return temperature_dic


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures_json = open('problem03_data.json', encoding='UTF8')
    temperatures = json.load(temperatures_json)
    print(turn(temperatures)) 
    # =>
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }