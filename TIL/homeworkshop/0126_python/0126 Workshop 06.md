# 0126 Workshop 06

### 1. 무엇이 중복일까

> 문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는 duplicated_letters 함수를 작성하시오.

```python
# 접근법
# 1. set으로 word의 중복된 문자열 제거
# 2. 그 set을 다시 list로 만들고, 그 list에 대해서 word.remove 돌림
# 3. word 리턴
def duplicated_letters(word):
    word = list(word) #string 타입은 .remove() 메서드가 없으므로, list로 변경
    clean_word = list(set(word))
    for cword in clean_word:
        word.remove(cword)
    return word
```

``` python
# 결과

duplicated_letters('apple') # --> ['p']
duplicated_letters('banana') # --> ['a','n','a']

#remove가 한번만 반복되서 같은 문자가 3개 이상 있는 경우는 거르지를 못한다.
#다시 set으로 변환해서 중복 제거하고 출력하자.
```

```python
# 수정 코드
def duplicated_letters(word):
    word = list(word) 
    clean_word = list(set(word))
    for cword in clean_word:
        word.remove(cword)
    word = list(set(word)) #for문 순회 이후 list->set->list 형 변형으로 중복 제거 후 반환
    return word
```

```python
# 결과

duplicated_letters('apple') # --> ['p']
duplicated_letters('banana') # --> ['a','n']
```

* 어찌저찌 잘 풀긴 했는데, 음... 형변환을 너무 해서 좀 조잡해보이는 감이 있다.
* 딕셔너리 자료형으로 썻어도 잘 할 수 있었을듯, 각 문자 리터럴을 키로 하고 value가 2이상인 친구들만 list로 변환해서 출력





### 2. 소대소대

>문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여 반환하는 low_and_up 함수를 작성하시오. 이때 전달 받는 문자열은 알파벳으로만 구성된다.

```python
# 접근법
# 1. 일단 싹 다 소문자로 변환
# 2. 소/대 카운트할 cnt 변수 생성
# 3. 각 문자열 순회하면서 소문자, 대문자 변환
# 4. cnt가 짝수이면 소문자로, 홀수이면 대문자로 변경
def low_and_up(word):
    word = list(word.lower())
    cnt = 0
    for idx in range(len(word)): # str 타입은 item assignment가 안되서 list로 바꿈
        if cnt % 2 == 0 :
            word[idx] = word[idx].lower()
        else:
            word[idx] = word[idx].upper()
        cnt += 1
    result = ''.join(word)
    return result
```



```python
# 결과
low_and_up('APPLE') # -> 'aPpLe'
low_and_up('banana') # -> 'bAnAnA'
```



### 3. 숫자의 의미

> 정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 이때, 제거된 후 남은 수들이 담긴 list들의 요소들은 기존의 순서를 유지해야한다.



```python
# 접근법

# 0. 중복을 제거해야겠지만, return 값에 순서가 있어야 하므로, set은 사용할 수 없다.
# 1. remove 메소드를 무수히 많이 돌린 후 그 결과를 반환할까봐도 생각했는데, 출제의도와는 다른 것 같다.
# 2. 따라서, 빈 리스트 tem_list를 하나 만들고, 조건에 맞는 리터럴만 append(혹은 extend) 하자.
# 3. 각 리터럴을 추려서 다른 리스트에 넣어야하므로, 인덱스 통한 접근을 해야한다.
# 4. for range 문과 무관한, 이전 문자를 뜻하는 변수 tem_letter를 만들자
# 4.1 만일 for문 순회 중, 현재 문자와 tem_letter가 동일하다면, 해당 루프 생략
# 4.2 만일 다르다면, 현재 문자 append. tem_letter 변경
# 5. return tem_list

def lonely(list_1):
    tem_list = []
    tem_letter = 'ㄱ' # 이전 값을 받아 줄 임시 변수
    for idx in range(len(list_1)): # element = int
        if tem_letter == list_1[idx]:
            continue
        else: # tem_letter != list_1[idx]
            tem_list.append(list_1[idx])
            tem_letter = list_1[idx]
    print(tem_list)

```



```python
# 결과

lonely([1,1,3,3,0,1,1]) # [1,3,0,1]
lonely([4,4,4,3,3]) # [4,3]
```











