def IamBrutal(key,sentence):
    l_key = len(key)
    l_sen = len(sentence)
    i,j = [0,0]
    cnt = 0
    while j<l_sen:
        if key[i] != sentence[j]:
            j = j-i
            i = -1

        i+=1
        j+=1

        if i == l_key:
            print(f"{key}는 sentence의 {j-l_key}부터 {j-1}에 있습니다.")
            i = 0
            cnt += 1
    return cnt


print(IamBrutal('abc','eeeabceeeabc'))