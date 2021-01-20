# 0120 workshop



# 1. List의 합 구하기

> 정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 bulit-in함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
def list_sum(int_list):
    total = 0
    for number in int_list:
        total += number #정수로만 이루어진 list가 전달되므로,연산자를 통한 정수연산이 된다.
    return total
```

```python
# result
list_sum([1,2,3,4,5]) --> 15
```



# 2. Dictionary로 이루어진 List의 합 구하기

> Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 bulit-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
def dic_list_sum(dic_list):#dic_list =[{'name' :'kim','age':12}, 
    								#  {'name' :'lee','age':4}]
    total = 0
    for i in range(len(dic_list)): #len(dic_list) = 2
        total += dic_list[i]['age'] # dic_list[0]['age'] == 12
        							# dic_list[1]['age'] == 4
    return total
```

```python
#result
dic_list_sum([{'name' :'kim','age':12},
               {'name' :'lee','age':4}]) --> 16
```





# 3. 2차원 List의 전체 합 구하기

> 정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
def all_list_sum(all_list):#all_list =[1],[2,3],[4,5,6],[7,8,9,10]/type :tuple
    total = 0 #합계 반환 값
    for idx in range(len(all_list)):#all_list는 길이가 4인 1개의 tuple이다.
        							# 따라서 idx는 range(0,4)를 갖는다.
        for num in range(len(all_list[idx])):#all_list[idx] -->[1],[2,3]...
            								 #튜플 내에서 indexing 한다.
                					#num는 all_list[idx]의 길이만큼의 range를 갖는다
            total += all_list[idx][num] 
            #이렇게 튜플의 각 리스트의 리터럴에 접근하여, 그 합을 구한다.
    return total


```

```python
#result
all_list_sum([1],[2,3],[4,5,6],[7,8,9,10]) --> 55
```





# 4. 교수님께 전하고 싶은 말

* 문제 조건에서 sum()을 사용하지 말라고 했는데, 저는 이번 문제를 풀면서 오히려 sum()을 어떻게 사용할 수 있는지 상상하지 못했습니다.  sum()을 이용한 풀이법도 알고 싶습니다.



* 항상 좋은 강의로 지식의 지평을 넓혀주셔서 감사합니다.