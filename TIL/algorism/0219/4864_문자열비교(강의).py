import sys

sys.stdin = open("input_4864.txt","r")

def brutal(p,t):
    # i는 텍스트를 위한 인덱스 :0부터 텍스트의 길이에서 패턴의 길이를 뺀 만큼 탐색
    for i in range(len(t)-len(p)+1):
        # j는 패턴을 위한 인덱스

        #is_ok = True # for else 대신에 변수 활용 가능
        for j in range(p): # p[j] 는 패턴의 위치를 나타냄. 패턴의 값들이 텍스트의 값과 같은지 확인
            if p[j] != t[i+j]:
                break
            else:
                return 1
        #if is_ok:
        #    return 1



def brutal2(p,t):
    i=0 # t 텍스트를 컨트롤 하는 인덱스
    j=0 # p 패턴을 컨트롤 하는 인덱스

    # j가 패턴의 길이가 되었을때, 찾았다면 멈춘다.
    # i 가 텍스트의 길이가 된다면 멈춰준다.
    while j < len(p) and i < len(t):
        if p[j] != t[i]:
            i = i-j # 시작 위치로 돌아간다
            j = -1 # j도 시작위치로 돌아간다. 
        
        i+=1
        j+=1
        if j == len(p): # 패턴을 찾았다.
            return 1
        else:
            return 0








T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    