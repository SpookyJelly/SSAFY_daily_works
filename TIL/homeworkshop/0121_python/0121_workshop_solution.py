'''
1. 숫자의 의미

문제에 나와있는 아스키 코드 표를 보면,
숫자와 문자가 1:1로 매핑이되어있는 것을 볼 수 있습니다.
예시 입력값인 (85, 115, 65, 102, 89)를 PDF의 표에서 찾아보니 각각 SaAfy에 해당하네요.
만약 여기서 "직접 딕셔너리로 저 표를 만들어서 사용해야겠다"라는 생각이 드셨다면.... 아주 훌륭합니다!
하지만 조금 번거로운 일이고 노동에 가까운 일을 과제로 드렸을 리는 없으니... 구글링을 해봅니다!

"python alphabet to number"이라는 검색어로 구글링을 해보니 ord()라는 함수가 나옵니다.
글자를 숫자로 바꿔주는 함수라는데, 그 반대도 있는지 확인해보니 chr()라는 함수도 있는 것 같습니다.
즉, 파이썬 내장 함수 중에 ord() 와 chr()이라는 친구가 있으니 그걸 활용해보면 될 것 같네요.

(두 내장 함수 관련한 자세한 내용은 아래 파이썬 공식문서를 통해 확인해주세요)
- https://docs.python.org/3/library/functions.html#ord
- https://docs.python.org/3/library/functions.html#chr
'''
def get_secret_word(numbers):
    word = ''

    # 1. 리스트를 순회하면서 번호를 하나씩 꺼낸다.
    for number in numbers:
        # 2. 번호를 아스키 표 상의 문자로 바꾸는 함수 chr()을 사용한다.
        letter = chr(number)
        # 3. 글자를 바깥에 빈 문자열을 만들어놓고 거기에 "이어붙입니다."
        word += letter

    # 4. 반복문 종료 후 (모든 숫자가 글자로 변환되었겠죠) 위에서 만든 글자를 반환합니다.
    return word

print(get_secret_word([83, 115, 65, 102, 89]))


'''
2. 내 이름은 몇일까?

위에서 본 문제와 거의 동일합니다.
우선 입력으로 들어오는 "문자열"에서 단어 하나씩 꺼낸 뒤,
아스키 표에서 대응되는 숫자를 찾으면 되겠네요.
그리고 각각의 숫자를 다 더해버리면 끝!
'''
def get_secret_number(word):
    total = 0

    # 1. 문자열을 순회하면서 (문자열은 리스트, 딕셔너리와 마찬가지로 for문을 이용하여 순회가능하죠.)
    for letter in word:
        # 2. tom이라면 t, o, m 하나씩 letter라는 이름으로 나올테니
        # ord() 함수를 이용하여 숫자로 바꿔줍니다.
        number = ord(letter)
        # 3. 바깥에 변수를 하나 만들어놓고 거기에 다 더해줍니다.
        total += number

    # 4. 반복문 종료 후 다 더해진 total값 반환해줍니다.
    return total

print(get_secret_number('tom'))


'''
3. 강한 이름

1번과 2번을 응용한 문제라고 볼 수 있죠.
나머지 로직은 다 똑같고, 두 문자열을 숫자로 변환했을 때
어느 쪽이 더 큰지 조건문으로 비교만 해주면 됩니다.
'''
def get_strong_word(word_1, word_2):
    word_1_total = 0
    word_2_total = 0

    # 1. 첫번째 문자열부터 숫자로 반환합니다.
    for letter in word_1:
        word_1_total += ord(letter)

    # 2. 두번째 문자열도 마찬가지로 숫자로 반환해줍니다.
    for letter in word_2:
        word_2_total += ord(letter)

    # 3. 두 숫자 중 더 큰 쪽을 조건문으로 물어보고
    # 더 큰 쪽의 "단어"를 반환합니다.
    if word_1_total > word_2_total:
        return word_1
    else:
        return word_2

print(get_strong_word('z', 'a'))
print(get_strong_word('tom', 'john'))

