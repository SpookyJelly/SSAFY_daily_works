import random

numbers = range(1,46)
lotto = random.sample(numbers,6) # random.sample(A,int) --> A라는 항목에서 int개의 샘플을 반환함
#.sample은 비복원 추출 // .choices는 복원 추출
lotto2 = random.choices(numbers,k=6) #k 크기만큼의 항목 추출
print(lotto)
print(lotto2)
print(f'이번 주 행운의 로또 번호는 {lotto}입니다!') # 문자열 리터럴 따옴표로 감싸기 전에 f를 쓰면 문자열 내에서도 변수 사용이 가능하네??
#근데 인덱싱해서 리터럴 빼오는건 안되네.. 이거 좀 자세히 알아봐야겠다.
print(f'이번 주 행운의 로또 번호는 {sorted(lotto)}입니다!')