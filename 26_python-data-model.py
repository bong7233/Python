# 파이썬 데이터모델 , 추상화

# 객체 -> 파이썬 데이터 추상화(overriding)
# 객체는 id로 type은 value로

# 일반적튜플
# 두점사이 거리구하기

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
# 이렇게 적으면 이게뭔지? 이름만으로는 파악하기 힘든경우가 많다
from math import sqrt


l_leng1 = sqrt((pt1[0]-pt2[0])**2 +(pt1[1]-pt2[1])**2) 
print(l_leng1)


# 네임드튜플 사용
# 튜플인데 dictionary 성격을 가지고있음(데이터 가공이 특이함)

from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')
# 선언방식이 class와 유사하다
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3) # Point(x=1.0, y=5.0)
print(pt4) # Point(x=2.5, y=1.5)
# 확인하기가 매우 편하다

l_leng2 = sqrt((pt3.x-pt4.x)**2 +(pt3.y-pt4.y)**2) 
print(l_leng2)

# 네임드 튜플 선언방법 전부 (4가지)
Point1 = namedtuple('Point', ['x','y'])
Point2 = namedtuple('Point', 'x,y')
Point3 = namedtuple('Point', 'x y')  
Point4 = namedtuple('Point', 'x y x class', rename=True)  # rename의 디폴트는 false

print(Point4) # 타입이 클래스형태로나옴


# Dict to Unpacking  딕셔너리로 넘어온걸 네임드튜플로 타입캐스팅
temp_dict = {'x':75, 'y':55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(10, 35)
p3 = Point3(10, y=20)
p4 = Point4(10, 35, 20, 45)
p5 = Point2(**temp_dict)
 # 딕셔너리형태를 **로 한번에 받음
print()

print(p1)
print(p2)
print(p3)

# rename 테스트
print(p4) #Point(x=10, y=35, _2=20, _3=45) 임의의 변수를 만들어서 저장함
# rename=False 라면 코드자체가 에러난다는걸 기억
print(p5) #Point(x=75, y=55)

# 사용해보기
print(p1[0]+p2[1])
print(p1.x + p2.y)

x, y =p3 #언패킹
print(x,y)


# 네임드튜플의 method
temp = [52,38]

# _make() : 네임드튜플로 새로운 객체생성
p4 = Point2._make(temp)
print(p4) #Point(x=52, y=38)

# _fields : 필드네임확인(key값이 뭐있나 조회)
print(p1._fields) #('x', 'y')

# _asdict() : OrderedDict 반환(네임드 튜플을 정렬된 딕셔너리로 반환)
print(p1._asdict()) #{'x': 10, 'y': 35}


# 실 사용예시
# 한반에 20명씩 4개반 ABCD

Classes = namedtuple('Classes', 'rank, number')

numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

# List Comprehension
students = [Classes(ranks, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

# 더 좋은방법
students2 = [Classes(rank, number) 
            for rank in 'A B C D'.split() 
                for number in [str(n) for n in range(1,21)]]

# 깔끕하게 출력해보기
for s in students2:
    print(s)