# 매직메소드
# special method  공식명칭
# 파이썬 핵심은 데이터모델
# 데이터모델이란 -> 시퀀스(sequence), 반복(iterator), 함수(functions), 클래스(class)
# 클래스안에 정의할수 있는 특별한(Built-in) 메소드 // 이미 설치되어있다
# 평소 클래스에서 사용해봤던 __init__ 같은애들


# 기본형 -> 지금까지 그냥 쓴 것들이 이미 클래스화 되어있다
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10  # 평소 그냥사용하던 변수들도 클래스에 들어갔던거다
print(type(n))

# 즉 +라는 표현이 .__add__ 를 내부적으로 저절로 호출한것
print(n+100)
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(),bool(n))
print(n * 100, n.__mul__(100))
##############################

# 클래스예제 (일반적이라면 클래스+클래스는 불가능 but 매직메소드를쓰면?)
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name,self._price)

    def __add__(self, x):
        return self._price + x._price * 0.8

    def __sub__(self, x):
        return self._price - x._price

    def __le__(self, x):
        if self._price <= x._price:
            return True
        else:
            return False
    def __ge__(self, x):
        if self._price >= x._price:
            return True
        else:
            return False

# 인스턴스생성
s1 = Fruit("banana", 3000)
s2 = Fruit("pineapple", 5000)

# 쉽게 가격만 더해보자 매직메소드로
# 원래는 __add__는 그냥 더하기지만, 매직메소드를 다시정의함으로써 바꿔서
# * 0.8 같은 조건까지도 한번에 포함가능
print(s1 + s2)
print(s1 - s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1)
print(s2)
#만약 매직메소드를 안쓰면 길고 가독성 낮아짐
#덧샘하려면 print(s1._price + s2._price)
