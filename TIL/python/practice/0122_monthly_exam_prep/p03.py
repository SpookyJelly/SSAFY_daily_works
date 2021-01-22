'''
A Word In A Sentence

어떤 단어와 문장이 주어질 때 해당 단어가 주어진 문장 속에 존재하는지 판별하는 함수를 작성하시오. 
만약 단어가 문장 속에 존재한다면 True, 그렇지 않으면 False를 반환합니다.

---
[입력 예시]
'Python', 'Life is short, you need Python.'

[출력 예시]
True
'''

def find_word_in_sentence(word, sentence):
    if word in sentence:
        return True
    return False


if __name__ == '__main__':
    # 아래 코드는 바꾸지 않습니다.
    print(find_word_in_sentence('Python', 'Life is short, you need Python.')) 
    #=> True

    print(find_word_in_sentence('Growth', 'The wound is the place where the light enters you.'))
    #=> False