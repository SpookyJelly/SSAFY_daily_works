# 0125 Homework 05

## 1. 평균점수 구하기

> key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의 평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.

```python
# 접근방법
# 1. value의 총 합을 저장할 변수 생성 
# 2. 사전의 각 value에 접근
# 3. for 문을 이용해 전부 더함
# 4. 평균 값을 계산해서 return
def get_dict_avg(dicti):
    total_value = 0 
    key_list = list(dicti.keys()) 
    # list()를 사용하지 않으면 dict_keys 객체가 반환되기에, 반드시 list()를 써야한다.
    for key in key_list:
        total_value += dicti.get(key)
    return total_value / len(key_list)
```

* 결과

```python
print(get_dict_avg({
    '파이썬' :80,
    '알고리즘' : 90,
    '장고' : 89,
    '웹' : 83
    })) # --> 85.5
```



## 2. 혈액형 분류하기

> 여러 사람의 혈액형(A,B,AB,O) 에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수 인 dictionary를 반환하는 count_blood 함수를 작성하시오.

```python
# 접근방법
# 0. 딕셔너리의 key/ value 쌍을 추가하는 for문 생성해야한다.
# 1. 딕셔너리는 존재하지 않는 key / value 쌍을 받는다면, 알아서 그 쌍을 추가하는 성질을 가지고 있다.
# 2. .get(x,i) 메소드를 이용해서, key에 맞는 value를 뽑을 수 있고, 만약 존재하지 않을시, 초기값도 지정		할 수 있다.
# 위 사실에 입각하여 코딩을 하자.

def count_blood(list_1):
    blood_dic = {} #0. 빈 딕셔너리 생성.(set 아님!)
    for blood in list_1: # 0. blood 임시변수를 blood_dic의 key로 활용할 것이다.
        blood_dic[blood] = blood_dic.get(blood,0)+1 
        # blood 는 list_1을 순회하면서 달라지고, 그때마다 위 식을 거친다.
        # blood_dic.get(blood)는 현재 blood_dic에서의 blood의 value를 반환하고, blood가 등장할때
        # 마다 +1씩 된다. 만약 blood가 blood_dic에서 처음 등장한 변수라면, 초기값을 0으로 하여
        # key / value 쌍을 추가한다.
    return blood_dic # blood_dic 사전형 반환
```

* 결과

  ```python
  count_blood(['A','B','A','O','AB','AB','O','A','B','O','B','AB'])
  # {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
  ```

  

  