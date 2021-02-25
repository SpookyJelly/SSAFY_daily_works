N_list = list(map(int,input().split()))

triple,run,cnt = [0,0,0]

# triple을 체크하는 부분
# 기본 아이디어 : 0~9의 범위로 리스트 각 리터럴 조사.
for i in range(0,10):
    for num in range(len(N_list)):
        # 만약에 리터럴이 현재 i와 같다면, cnt는 1 올라가고, 그게 3개이면 tripe 취급
        if N_list[num]==i:
            cnt += 1
            #i 는 num 루프동안 고정이니까, 각 숫자가 리스트에 몇개 있는지 test가 된다.
            if cnt == 3:
                triple +=1
                cnt = 0
    cnt = 0

# run을 체크하는 부분
# N_list 전체를 대상으로 시행
for j in N_list:
    # 만약에 연속된 부분이 있으면, run을 1올림.
    # 연속된 부분의 가장 작은 요소를 대상으로 검사하므로, 중복 체크의 염려가 없다.
    if j in N_list and j+1 in N_list and j+2 in N_list:
        run += 1


# baby-gin이 되려면, [triple,run] 이 [0,2],[1,1],[2,0] 인 경우 뿐이다.
# 이들의 공통점은 합이 2라는 것이다. 따라서 이 둘의 합이 2이면 baby-gin으로 간주해도 된다.

if triple+run == 2:
    print("Baby-gin 입니다.")
else:
    print("Baby-gin이 아닙니다.")
    print('run',run,'T',triple)