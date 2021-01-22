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
    text1_list = list(sorted(text1))
    text2_list = list(sorted(text2))
    if text1_list == text2_list:
        return True
    else:
        return False


# sorted 안 써보고 해보려한 함수인데, 알파벳 갯수를 카운팅 못해서 실패한 케이스
# 다른 방식의 cnt가 필요할것이라 생각합니다.
# def check_anagram(text1, text2):
#     cnt = 0
#     text1_list = list(text1)
#     text2_list = list(text2)
#     for word in text1_list:
#         if word in text2_list:
#             cnt +=1
#         else:
#             pass
#     if cnt == len(text1_list):
#         return True
#     else:
#         return False


if __name__ == '__main__': 
    print(check_anagram('ohlamesaint', 'themonalisa')) # True
    print(check_anagram('apple', 'eppla'))             # True
    print(check_anagram('banana', 'babana'))           # False