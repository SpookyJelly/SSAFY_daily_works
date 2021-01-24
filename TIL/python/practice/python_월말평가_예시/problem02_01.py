import json
# 접근 방법
# - restorant가 사전형 자료이므로, 키 값만 잘 추리면 된다.
# 1. restorant의 key인 'menus'를 호출한다.
# 2. 호출한 values로 새로운 리스트를 만든다. (원본을 이용하면 생략가능)
# 3. 리스트의 길이를 잰다.
# 4. 길이를 반환한다.

def menu_count(restorant):
    menus = restorant['menus']
    return len(menus)
    
    '''
    여담으로, return print(len(menus))로 작성하게 된다면,
    결과는 

    4
    None

    이 출력된다. 최초의 4는 menu_count(restorant) 함수 내부에서 작성된
    print(len(menus)) 때문에 출력된다. 그러나 print() 함수는 None 타입을
    가지고 있다. 그리하여 return print(~~) 에 의해 menu_count(restorant)는 None
    을 반환하게 되고, print(menu_count(restorant)) --> print(None) --> None
    이 되는 것이다.


    '''

    ''' 
    len 함수 사용하지 않은 버젼

    menus = restorant['menus']
    cnt = 0 # menus의 요소를 카운트 해준 결과를 저장할 변수
    for menu in menus: 
        cnt += 1  
        
    # 해당 for문은 menus의 모든 요소를 menu로 할당하여 반복된다.
    # 따라서 , cnt 는 menu의 수 만큼 1씩 증가하게 된다. 

    return cnt

    
    '''
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    restorant_json = open('problem02_data.json', encoding='UTF8')
    restorant = json.load(restorant_json)
    print(menu_count(restorant)) 
    # => 4