import json
# 접근 방법
# 1. 리스트의 각 요소에 접근 (json 파일 보면 scores는 리스트 꼴임)
# 2. 변수 간 1대1 대소 비교.
# 3. 만약, 이전 최대값보다 현재 변수가 더 크다면, 최대값 변경
# 4. 루프 종료 후 최대 값 반환.


def max_score(scores):
    ''' 
    return max(scores)
    
    이거면 한방에 끝인데, 평가의 의도는 이것이 아니니,
    가급적 반복문과 조건문으로만 풀자

    '''
    maxi = 0 # 최고점을 받아 반환할 변수 maxi를 초기화
    for score in scores: #scores 리스트에 있는 리터럴들을 score로 선언
        if score > maxi:
            maxi = score
    return maxi

    '''
    while 문 사용한 버젼
    
    # 종료 조건 : 리스트의 끝
    
    n = len(scores)-1 // 리스트의 인덱스는 0부터 시작하므로 -1해서 싱크로 맞췄다. 
    maxi = 0

    while(n>0): // 한번 루프 마다 -1, scores만 순회하고 종료
        if scores[n]>maxi:
            maxi = scores[n]
        n -= 1
    return maxi
    
    '''


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json', encoding='UTF8')
    scores = json.load(scores_json)
    print(max_score(scores)) 
    # => 90