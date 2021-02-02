# class
# OPP(객체 지향 프로그래밍)
# class instance
# self 개념
# instance method

# class 와 instance의 차이를 이해 point
# 인스턴스와 객체의 차이점을 찾아서 이해하기 필수
# 네임스페이스 : 객체를 인스턴스화 할때 저장된 공간(dict형태)
# 클래스변수 : 직접 접근 가능
# 인스턴스 변수 : 객체마다 별도 존재

class Dog(object):
    pass #(object)는 생략가능하며 Dog, Dog(), Dog(object)는 같은표현

    #클래스의 속성
    species = 'firstdog'  # 클래스변수

    # 초기화/인스턴스속성 = 모든 클래스는 초기화인스턴스를 가짐.
    def __init__(self,name,age): # 클래스가 초기화될떄 반드시 호출되는 함수
        self.name = name
        self.age = age
#-----------------------------------여기까지가 class 만들기 (틀만들기)

# 인스턴스는 객체에 속함 이라고 일단개념을 세워놓기

print(Dog)

# 인스턴스화/ 하나의 class를 가지고 변수를 통해 값이 들어가는것
a = Dog("mikky",2)
b = Dog("baby", 3)
# 이 각각의 미키와 베이비는 인스턴스

# 네임스페이스 .__dict__ 를통해서 내부공간에 뭐가들어있는지 봄
print('dog1', a.__dict__) # 인스턴스 a의 네임스페이스에는 미키라는이름과 2살
print('dog2', b.__dict__) # 인스턴스 b의 네임스페이스에는 베이비라는이름과 3살 정보가 들어있음

Dog.species # species는 클래스메소드 이므로 클래스.메소드이름 으로 바로불러낼수있음
a.species
b.species # a,b 도 Dog라는 클래스안의 인스턴스이기떄문에 클래스매소드안에 포함됨.


## self의 이해
class SelfTest:
    def func1():
        print('func1 called')
    def func2(self):
        print(id(self))
        print('func2 called')

f = SelfTest()   # __init__이 없더라도 파이썬이 자동으로 인식
             
# print(dir(f)) # dir로 f라는 네임스페이스에 사용할수잇는 메소드가 뭔지본다.
# func1 과 func2가 실행가능 함수에 들어간것을 확인
# f.func1() =에러뜸,,, == func1은 self가없기때문에 f를 넣을수없음.(self가 f를 받아야 들어갈수잇음)
f.func2() # func2가 호출됨. -> self는 인스턴스를 필요로함. 즉 f 가 인스턴스로 들어간것
# 클래스를 인스턴스시킨 f의 id값과 self로 넘어온 id값이 같음.
# 즉 클래스안의 매개변수를 선언하는데 self가없다?
# = 클래스 매소드다(매개변수가 없기때문). 클래스로 바로직접호출해야#
# 그럼 self가 붙은것은 인스턴스 메소드이다. =>인스턴스를 넘겨주던가 인스턴스로 호출해야함
# f.func2 =인스턴스f로 호출 or SelfTest.func2(f) 인스턴스(f)를 넘겨줌.

#그래서 func1을 호출하려면
SelfTest.func1() # class로 바로접근해서 호출할수잇는 메소드가 됨.
SelfTest.func2(f) # func2는 self에 넣을 인스턴스값(f)를 넣어줘야 호출됨.



# 클래스변수와 인스턴스변수 연습
class WareHouse:
    #클래스변수 설정
    stock_num = 0 # 재고라고 생각하면됨

    def __init__(self, name):
        #인스턴스변수 = self가 있기때문
        self.name = name
        WareHouse.stock_num += 1 #재고를 하나 더함

    def __del__(self):
        WareHouse.stock_num -= 1 # 재고를하나  뺌

user1 = WareHouse('Lee')
user2 = WareHouse('John')  # 인스턴스 두개 생성

print(WareHouse.stock_num)  # 리와 존이 들어갈떄마다 1씩더해졋으니 스탁은 2가됨


# 네임스페이스접근
print(user1.__dict__)
print(user2.__dict__)
print(WareHouse.__dict__)
# dict햇을때 WareHouse에는 stock_num이있지만, user1 2 에는 없는것을 볼수있다
# 하지만 user.stock_num을 해도 값이나오는 이유는 파이썬이 똑똑하게 찾음
# 즉 user1 에 stock_num 함수가 없더라도. 상위 클래스의 네임스페이스로
# 이동해서 있으면 찾아서출력함.

del user1   # 유저1 삭제
print(WareHouse.__dict__) # stock_num이 1로 줄어든것을 볼수있음.
