import json
# 접근 방법
# 1. 60점 이상인 점수를 카운트할 변수 cnt 생성
# 2. 리스트의 각 요소 접근
# 3. 반복하면서, 60점 이상인 변수가 나오면 cnt += 1
# 4. cnt 반환

def over(scores):
    cnt = 0
    for score in scores:
        if score >= 60: # =의 위치가 헷갈리다면, "크거나 같다" / "작거나 같다" 로 외우자.
            cnt += 1
    return cnt
    
    '''
    while문 사용

    cnt = 0
    n = len(scores) - 1
    while (n>0):
        if scores[n]>=60:
            cnt += 1
        n -= 1
    return cnt

    '''

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json', encoding='UTF8')
    scores = json.load(scores_json)
    print(over(scores)) 
    # => 3