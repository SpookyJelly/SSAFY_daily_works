#5432 쇠막대기 자르기
# 2중 루프 짜면 100억번 도니까, 설계를 잘해야한다.

T = int(input())

for tc in range(1,T+1):

    iron_bar = input()

    cnt = 0 # 막대 수
    ans = 0 # 정답

    for i in range(len(iron_bar)):
        # 열린 괄호라면 막대 추가
        if iron_bar[i] =='(':
            cnt += 1
        else:
            # 닫힌 괄호라면 막대 감소
            # 레이져라면 당연히 잘못 세었으니까 뺴는 것이 맞다.
            # 아니라면 어차피 철봉 끝이니 빼는 것이 맞다.
            cnt -= 1
            # 레이저라면
            if iron_bar[i-1] =='(':
                # 레이져로 잘린 막대들이 생겼으니
                ans += cnt
            else:
                #막대 끝이라는 뜻
                ans += 1
    print("#{0} {1}".format(tc,ans))

# 이거 말고도 리스트를 만들어서 막대기를 저장하고 빼고 하는 방법..
# 스택을 이용한 방법이다.
# 가장 최근에 들어온게, 가장 최근에 나가는거 보니까...선입선출////맞다!
"""

for tc in range(1,int(input())+1):
    iron_bar = input()

    # 실제로 철봉이 담길 리스트
    s = []
    ans = 0

    for i in range(len(iron_bar)):
        #열린 괄호라면 s 리스트에 넣어놓기
        if iron_bar[i] =='(':
            s.append('(')
        else:# iron_bar[i] ==')'
            # 무조건 꺼내기
            s.pop()
            #레이저라는 뜻
            if iron_bar[i-1] == '(':
                ans += len(s)
            else:# 막대의 끝이라는 뜻
                # 짜배기 추가
                ans += 1

"""