# 파이썬 일급함수(객체)
# 일급함수 ? -> 함수형 프로그래밍이 가능
# 쉽게말해 기능별로 모듈화(함수화) 되어있기떄문에 부작용을 최소화
# 순수함수를 지향하며 여러 스레드에서 문제없이 작동하는 프로그래밍이 가능

# 파이썬 함수의 특징 (자바스크립트와 비슷)
# 1. 런타임 초기화 (실행시점에 초기화가됨)
# 2. 변수 할당 가능 (중요)
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)


# 함수 객체

# 5! = 5*4*3*2*1
def factorial(n):
    '''Factorial Function -> n :int '''
    if n == 1:
       return 1
    return n*factorial(n-1)

class A:
    pass

print(factorial(5)) # 120
print(factorial.__doc__) # 주석확인 good
print(type(factorial), type(A)) # class 'function', 'type'

# class가 아니라 함수인데도 class의 습성을 가짐
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)


# 변수할당
# 즉 함수를 변수에 할당해서 변수() 형태로도 사용할 수 있음
var_func = factorial
print(var_func)
print(var_func(10))
print(list(map(var_func, range(1,11))))

# 함수 인수전달 및 함수로 결과반환 -> 고위함수(Higher-order function)
# map, filter, reduce

# 두개다 동일한 결과가 나오지만, map 과 filter를 활용
print(list(map(var_func,filter(lambda x:x%2, range(1,6))))) # 홀수만 골라서 ! [1,6,120]
print([var_func(i) for i in range(1,6) if i % 2]) # [1, 6, 120]

# reduce
from functools import reduce
from operator import add

# 하나하나를 지워가면서 더해가는 함수
print(reduce(add, range(1,11))) # 55
print(sum(range(1,11))) # 55 -> 하지만 이게더 빠르고 읽기편하다

# 익명함수(lambda) -> 가급적 익명함수는 주석을 꼭 달아주는것이 권장
# 하지만 사용가능하다면 익명함수대신 일반함수를 사용하는것이 better
# 일반함수 형태로 리팩토링 권장

# 익명함수는 이런식으로 쓰는것이 best
print(reduce(lambda x, t:x+t, range(1,11))) # 55

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능한지 확인해야함
print(callable(str)) # True , callable() 함수로 바로확인가능
print(callable(var_func), callable(factorial)) # True
print(callable(3.14)) # False -> float은 콜러블이아니다 그냥 상수다

########################

## Partical 사용법 ( 매우매우 중요함, 많이 사용됨)
## 인수를 고정 -> 콜백함수 사용
from operator import mul
from functools import partial

print(mul(10,10)) # 100

# 인수고정
five = partial(mul,5) # mul 함수는 인수를 두개받아야하는데 일단 5만 적어줌
# 즉 mul(5, n) 의 형태로 동작

# 고정추가
six = partial(five, 6)

print(five(10)) # 50
print(five(100)) # 500
print(six()) # 30
print([five(i) for i in range(1,11)]) #[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(list(map(five,range(1,11)))) #[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

################################

# 클로저 기초
# 파이썬 변수 범위(scope)

def func_v1(a):
    print(a)
    print(b)

# func_v1(10) -> b가 선언되지않았으므로 error

# b 를 global변수로 선언해주면 정상작동
b=20
func_v1(10) # 10,20

# c 를 함수내에서 선언했는데, 만약 호출보다 아래있으면
# 전역변수를 불러오는게아니라 에러가 발생
# 즉 지역변수와 전역변수가 중복된다면 전역변수는 무시
c = 30
def func_v1(a):
    print(a)
    print(c)
    c = 40
# func_v1(10) 하면 c가 30으로 나올것같지만, 지역변수 c가잇으므로
# 지역변수 c를 불러옴, 하지만 호출보다 아래 선언되엇으므로 error

# 만약 함수내에 전역변수 선언을 해주면 지역내에서 전역변수를 수정가능
c = 30
def func_v1(a):
    global c
    print(a)
    print(c)
    c = 40

print(c) # 30
func_v1(10) # 함수 호출시 전역변수 수정이 일어남
print(c) # 40
################################


# 클로저 사용이유
# 서버프로그래밍 -> 동시성(Concurrency)제어 -> 메모리공간에 여러자원이 접근
# 결국 교착상태(Dead Lock) 발생
# 메모리를 공유하지않고 메세지 전달로 처리하기위한 방법
# 클로저는 공유하되 변경되진 않는다(Immutable, Read Only) -> 함수형프로그래밍
# 클로저는 불변자료 및 atom(일관성), STM 을통해 -> 멀티스레드(coroutine) 프로그래밍에 강점
# 한마디로, 클로저는 "(불변)상태를 기억한다"
# 외부에서 호출된 함수의 변수값,상태(레퍼런스)를 복사 후 저장 -> 후에 접근 가능


# a는 변하지않고 누적되지도않기에 각각 계산됨
a = 100
print(a+100) # 200
print(a+1000) # 1100 (1200이 아님)

#결과누적함수 사용
print(sum(range(1,51))) # 1275
print(sum(range(51,101))) # 3775

# 클래스이용
class Averager():
    def __init__(self):
        self._series = []
    def __call__(self,v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# class 인스턴스 생성
averager_cls = Averager()
print(dir(averager_cls)) # __call__ 이 있으므로 함수로써 호출가능

#누적 (클래스지만 함수형태로 썻음에도 누적효과를 줄 수있음)
# 즉 이렇게 누적가능하게 해주는것이 클로저의 역활
# 함수는 종료되었지만, 상태를 기억하고있음
print(averager_cls(10)) # 10 , 10을 기억
print(averager_cls(30)) # 20 , 20을 또 기억
print(averager_cls(50)) # 30 , 기억된걸 사용해서 연산


##### 클로저 심화사용 #####
## 클로저사용은 패턴이 거의 정형화 되어있으므로 익혀두면 편함
def closure_ex1():
    # Free variable (자유변수) ->클로저 영역 밖에서 선언된변수
    # 클로저 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series,len(series)))
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_ex1()

print(avg_closure1(10)) # 10
print(avg_closure1(20)) # 15
print(avg_closure1(30)) # 20 ,, 누적되는것을 확인가능


# function inspection , 함수내부 확인
print(dir(avg_closure1))
print(dir(avg_closure1.__code__)) # co_freevars 가 있음을 확인
print(avg_closure1.__code__.co_freevars) # series 가 나옴, 자유변수를 저장한것
print(avg_closure1.__closure__[0].cell_contents) # 10,20,30 입력된 값을들 저장하고있음


## 클로 사용주의점 (잘못된사용)
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total/ cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10)) -> 참조error 발생 cnt가 선언되기전에 참조되었다


# 그렇다면 nonlocal을 사용해보면 ??
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        # 위에서 선언한 free variable  cnt와 total을 사용
        # 즉 이제부터 상태와 레퍼런스를 저장하는 상태가됨
        nonlocal cnt, total
        cnt += 1
        total += v
        return total/ cnt
    return averager

avg_closure3 = closure_ex3()
print(avg_closure3(10)) # 10
print(avg_closure3(20)) # 15
print(avg_closure3(30)) # 20 , 정상작동함
