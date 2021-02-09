# 90도 중력 문제
# 중력의 영향으로 결국 막히는 부분도 없어지게 되므로,
# 최상단의 요소 이후 막히지 않은 부분을 카운트 하면된다

inp = [2,4,2,0,0,6,8,7,0]

# 각 리터럴에 대해서 반복
maxi = 0
for i in range(0,len(inp)-1):
    # 공백이 몇개인지 count 해주는 변수
    cnt = 0
    # i와 j 요소를 비교할 껀데, ,j는 i의 다음 요소이다.
    for j in range(i+1,len(inp)):
        if inp[i]>inp[j]:
            cnt += 1
        if maxi< cnt:
            maxi = cnt
print(maxi)