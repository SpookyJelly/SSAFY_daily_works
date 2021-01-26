#if __name__ == '__main__':
#이거 무슨 뜻일까
def func():
    print(__name__) # == __main__
    print(__file__) # 지금 내가 실행시키는 파일명

if __name__ == '__main__':
    # 현재 파일이 직접 실행되었는지
    # 판별하기 위한 조건문.
    # ex)python apple.py

    '''
    간접 실행?
    == 다른 파일에서 불러와져서 실행
    
    '''
    func() # __main__