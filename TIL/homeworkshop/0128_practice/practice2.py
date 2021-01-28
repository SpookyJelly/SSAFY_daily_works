# random 모듈에서 sample 메서드를 import 함
# ~놀라운 사실~ 클래스 선언할때, 모듈을 불러올 수 있다!
# 나는 클래스가 py 외에 새로운 생태계인줄 알았는데, 아니였다. 동일하게 import 가능
from random import sample

class ClassHelper:

    
    
    def __init__(self,student_list):
        self.student_list = student_list
        
    def pick(self,num):
        # A라는 변수가 이 함수 내에서 선언됨과 동시에 할당.자료형 결정?
        # 점 접근 안쓰고 변수를 만들어도 적용되는 이유가 이 함수 내에서만
        # 사용되는 변수라서? 임시변수 같은 느낌인가???
        A = sample(self.student_list,num)
        return print(list(A))
    
    # def match_pair(self):
    #     # sample
    #     pair_1 = ClassHelper.sample(self.student_list,2)
    #     pair_2 = set(self.student_list) - set(pair_1) #아니 뺴는거 안되잖아...set으로 쓸까?
    #     #return 
    #     print([list(pair_1),list(pair_2)])
    def match_pair(self):
        # 기본 아이디어
        # pair_1을 student_list에서 추리고, student_list - pair_1 = pair_2로 함
        # pair_1, pair_2 return
        # 근데 리스트는 차집합 연산이 안되므로, set 자료형으로 바꿔서 연산한다.
        result = []
        pair_1 = sample(self.student_list,2)
        pair_2 = set(self.student_list) - set(pair_1)
        while(True):
            result.append(pair_1)
            if len(pair_2) <=3 :
                
                result.append(list(pair_2))
                break
            else:
                
                pair_1 = sample(pair_2,2)
                pair_2 = set(pair_2) - set(pair_1)
        print(result)
ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피','서사피','금사피','남궁사피'])
ch.pick(3)
ch.match_pair()