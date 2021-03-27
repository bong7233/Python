# 파이썬 데이터모델 , 추상화

# 객체 -> 파이썬 데이터 추상화(overriding)
# 객체는 id로 type은 value로 취급

# 일반적튜플
# 두점사이 거리구하기

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
# 이렇게 적으면 이게뭔지? 이름만으로는 파악하기 힘든경우가 많다

# sqrt = 루트씌워주는 함수
from math import sqrt

# 두점사이의 거리구하기
# 되긴하는데 뭔가복잡하고 알아보기 힘들다
l_leng1 = sqrt((pt1[0]-pt2[0])**2 +(pt1[1]-pt2[1])**2) 
print(l_leng1)


# 네임드튜플 사용
# 튜플인데 key와 value를 가지는 dictionary 성격을 가지고있음(데이터 가공이 특이함)

from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')
# 선언방식이 class와 유사하다
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# 확인하기가 매우 편하다
# 인덱스로도 접근가능
# print(pt3.x) 해도 1.0 으로나옴, 접근이 매우 유연하다
print(pt3) # Point(x=1.0, y=5.0)
print(pt4) # Point(x=2.5, y=1.5)

# 인덱스로 접근해도 되지만, 실수를 줄이기위해 편하게 x,y 활용가능
l_leng2 = sqrt((pt3.x-pt4.x)**2 +(pt3.y-pt4.y)**2) 
print(l_leng2) # 3.80788...


# 네임드 튜플 선언방법 전부 (4가지)
Point1 = namedtuple('Point', ['x','y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')  

# 예약어인 class나 x가 중복되면 원래 오류가뜨지만 rename으로 방지함
# rename의 디폴트는 false
#이렇게하면 오류없이 네개를 받을수 있게됨
Point4 = namedtuple('Point', 'x y x class', rename=True)

print(Point4) # 타입이 클래스형태로나옴

# 딕셔너리를 네임드튜플에 할당하기
# Dict to Unpacking  딕셔너리로 넘어온걸 네임드튜플로 타입캐스팅
temp_dict = {'x':75, 'y':55}


# 객체 생성

#명시적으로 x,y를 언급해줄수도있음, 유연함
p1 = Point1(x=10, y=35)
p2 = Point2(10, 35)
p3 = Point3(10, y=20)
# 이렇게 argument가 많을땐 갯수가 틀리지않도록 주의
p4 = Point4(10, 35, 20, 45)

 # 딕셔너리형태를 **로 한번에 받음
 # 파이썬이 똑똑해서 딕셔너리의 x,y를 네임드튜플에 언패킹해서 집어넣음
p5 = Point2(**temp_dict)


print(p1)
print(p2)
print(p3)

# rename 테스트
# rename=False 라면 코드자체가 에러난다는걸 기억
# 하지만 이런 임의의 변수를 랜덤으로 만드는건 좋지않은것이므로 안쓰는것이좋음
#Point(x=10, y=35, _2=20, _3=45) _2,_3같은 임의의 변수를 만들어서 저장함
print(p4) 

print(p5) #Point(x=75, y=55)


# 만들어진값들 사용해보기
print(p1[0]+p2[1]) # 값이 잘 나오지만,, 이렇게쓰려고 네임드튜플쓰는게아니다
print(p1.x + p2.y) # 이렇게 간략하고 보기좋게만들수있음

x, y =p3 # x는x로 y는y로 언패킹
print(x,y)



# 네임드튜플의 method 활용해보기

# 리스트선언
temp = [52,38]

# _make() : 리스트를 네임드튜플로 새로운 객체생성(값의 갯수가 동일해야함)
p4 = Point2._make(temp)
print(p4) #Point(x=52, y=38)


# _fields : 필드네임확인(key값이 뭐있나 볼수있음)
print(p1._fields) #('x', 'y')

# 중요한 메서드
# _asdict() : OrderedDict 반환(네임드 튜플을 정렬된딕셔너리로 반환)
print(p1._asdict()) # OrderedDict([('x': 10, 'y': 35)])


# 실습해보기
# 한반에 20명씩 4개반 ABCD 만들기

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹리스트 선언
# list comprehension
# 1번~20번 만들기
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()

print(numbers) # ['1', '2', ... '20']
print(ranks) # ['A','B','C','D']

# List Comprehension
students = [Classes(ranks, number) for rank in ranks for number in numbers]

print(len(students)) # 80
print(students) # [Classes('A','1')..., Classes('D','20')]


# 더 좋은방법 가독성 살리기 
students2 = [Classes(rank, number) 
            for rank in 'A B C D'.split() 
                for number in [str(n) 
                    for n in range(1,21)]]

# 깔끕하게 출력해보기
# print 이용해서 줄바꿈해서 깔끔
for s in students2:
    print(s)
