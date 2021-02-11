# 외장함수
# 종류가 셀수없이많지만, 자주사용하는것위주로보기

# sys
import sys
print(sys.argv) # 구글검색해서 알아보기
# sys.exit() 강제종료함수. 사용을 반드시 조심해야함.
print(sys.path) # 현재 있는 모든 패키지들의 위치를 표시


# pickle 객체파일을 임시로 읽고쓸때 주고사용(머신러닝 데이터 쪽에서 자주씀)
import pickle
# 쓰기
f = open("파일이름.obj", 'wb') # writebinary
obj = {1: 'python', 2:'study', 3:'basic'}
pickle.dump(obj, f)
f.close()
# 읽기
f = open('파일이름.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()


# os : 환경변수, 디렉토리(파일) 처리관련, 운영체제 작업관련
# mkdir, rmdir(비어있으면삭제), rename
import os
print(os.environ) # 지금 운영체제(os)관련정보를  !!dict 형태로!! 반환
print(os.environ["ATOM_HOME"]) # 해당파일의 위치

#현재 경로를 확인
print(os.getcwd()) # 지금기준은 파이썬파일을 실행하고있는경로


# time : 시간관련처리
import time
print(time.time()) # 현재 시간인데 알아보기힘듦
print(time.localtime(time.time())) # 형태변환, 하지만복잡;
print(time.ctime()) # 간단한 요일 월 일 시간 년 순으로 나옴
# 원하는 형식으로 표현가능
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

#시간간격 설정
for i in range(5):
    print(i)
    time.sleep(1) # 1초마다 실행


# random : 난수리턴~
import random

print(random.random()) # 0~1사이의 실수
print(random.randint(1,45)) # 정해준 수 중 정수
print(random.randrange(1,45)) # randint와 같음

# shuffle
d = [1,2,3,4,5]
random.shuffle(d)
print(d)

# 무작위선택
c = random.choice(d) # Itrable한 객체여야함
print(c)

# webbrowser : 본인 os의 웹 브라우저 실행

import webbrowser

webbrowser.open("http://google.com") #페이지 실행
webbrowser.open_new("http://google.com") # 새로운창에서실행
