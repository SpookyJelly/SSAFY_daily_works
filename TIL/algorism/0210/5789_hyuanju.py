# 5789번 현주의 상자 바꾸기
"""
현주는 1번부터 N번까지 N개의 상자를 가지고 있다. 
각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0으로 적혀있다.
숫자가 너무 단조로웠던 현주는 다음 Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경하려고 한다. 변경하는 방법은 다음과 같다.
i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
현주가 Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을 순서대로 출력하는 프로그램을 작성하라.



[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 두 정수 N, Q (1 ≤ N, Q ≤ 103)가 공백으로 구분되어 주어진다.
다음 Q개의 줄의 i번째 줄에는 Li, Ri (1 ≤ Li ≤ Ri ≤ N)이 주어진다.

"""
# 접근 방법 : 삼성 버스 정류장 문제를 응용한다.
# N개의 0으로 가득찬 리스트를 미리 만든 다음, 거기에 작업 Q의 조건에 맞을때마다 값을 변동 시킨 후 출력
for tc in range(1,int(input())+1):
    N,Q = map(int,input().split()) # N :리스트의 길이 Q: L R 범위 입력자
    # 1번 박스부터 N번 박스 까지 있으므로, boxes 변수와의 인덱스를 맞추기 위해 의미없는 리터럴 space를 삽입
    boxes = ['space'] + [0] * N
    for lr in range(1,Q+1):
        L,R = map(int,(input().split()))
        # 버스 정류장 때처럼, L/Q 범위 내의 값을 Q의 시행횟수. lr로 바꾼다.
        for idx in range(L,R+1):
            boxes[idx] = lr
    boxes = [str(c) for c in boxes[1:] ]
    print('#{0} {1}'.format(tc, ' '.join(boxes)))