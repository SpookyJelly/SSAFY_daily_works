'''
애너그램

애너그램(anagram)은 단어나 문장을 구성하고 있는 문자의 순서를 바꾸어 다른 단어나 문장을 만드는 놀이입니다.
두 문자열이 공백으로 구분되어 입력된다고 했을 때, 서로 애너그램인지 판별하는 함수를 작성하시오.
입력 문자는 모두 소문자로 빈칸 없이 제공됩니다.

---
[입력 예시]
ohlamesaint themonalisa

[출력 예시]
True
'''

def check_anagram(text1, text2):
    '''
    sorted()를 이용한 방법도 좋은 접근입니다.
    하지만 아래처럼 딕셔너리를 활용한 방법도 한 번 고민해보세요.
    코드 자체도 훨씬 효율적이고, 우리가 배운 내용을 복습하기도 좋을거에요.
    '''

    text_dict = {}

    for letter in text1:
        if letter in text_dict:
            text_dict[letter] += 1
        else:
            text_dict[letter] = 1
    
    for letter in text2:
        if letter in text_dict:
            text_dict[letter] -= 1
        else:
            text_dict[letter] = 1

    for value in text_dict.values():
        if value != 0:
            return False

    return True

if __name__ == '__main__': 
    print(check_anagram('ohlamesaint', 'themonalisa')) # True
    print(check_anagram('apple', 'eppla'))             # True
    print(check_anagram('banana', 'babana'))           # False