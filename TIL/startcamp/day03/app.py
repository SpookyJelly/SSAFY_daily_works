# 인생 최초의 서버 생성.
# That's one small step for man, one giant leap for mankind
from flask import Flask
app = Flask(__name__)
# @app.route() 이하로 정의된 함수들은 해당 페이지로 접속하면 자동으로 실행이 된다.
@app.route('/')
def hello_world():
    return 'Hello, World!'

# http://127.0.0.1:5000/name
@app.route('/name')
def name():
    return '안녕하세요, 접니다.'


# 127.0.0.1 == local host == 내 컴퓨터 라는 소리임