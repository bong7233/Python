# 함수 function
# 코드의 안정성 enhence/ 코드의 수정에 편리/
# function 에서 입력값 = > 출력값 같은 type //
# 함수의 함수식 및 Lambda

# 함수 정의 방법
# def function_name(parameter):
#   code    형태


# w = 인수 = parameter
def first_func(w):
    print("Hi,", w)

word = "Keep going"

first_func(word)

def return_func(w1):
    value = "bye," + str(w1)
    return value
############### 함수형 프로그래밍 찾아서 듣기 (파이썬에 도움이많이됨)
x = return_func('good')
print(x)

# 다중반환

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3
print(func_mul(5))
x, y, z = func_mul(3)   # 각각의 요소를 따로 설정해서 뺼수도 있
print(func_mul(3))
print()
func_mul(5)
print()
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3) # return 값을 튜플로 지정하면 나오는값도 튜플로나옴(응용가능)


q = func_mul2(10)

print(type(q))

############## 그럼 list로 return 가능할까?
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

l = func_mul3(10)

print(type(l), l)

################## dict도 가능??

def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1':y1,'v2': y2,'v3': y3}

d = func_mul4(10)

print(type(d), d, d.get('v2'), d.items(), d.keys())


# 중요함 /////////////
# *args, **kwargs
# *args (unpacking)
def args_func(*args): #매개변수명은 자유지만 통상적 args tuple형태로 매개변수를넘김
    for i, v in enumerate(args):
        print('Result : {}'.format (i),v)

args_func('Lee')
args_func('Lee','Park','Jason')

# **kwargs (unpacking) key value로 매개변수를 넘김 == 튜플보다 정확함 kv가있어서
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])

kwargs_func(name1='Lee', name2='park', name3='Joe', send=False)


# 전체 혼합
def exam(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)

exam(10, 20, 'lee', 'kim', 'park', age1=20, age2=30, age3=400)

# 중첩함수

def nested_func(num):
    def fun_in_fun(num):
        print(num)
    print("in fun")
    fun_in_fun(num +100)

nested_func(100)

############# Lambda ##############
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체생성 -> 리소스(메모리) 할당
# 람다는 즉시실행함수 (heap) -> 메모리 초기화
# 너무 많이쓰면 가독성이 오히려감소

def mul_func(x, y):
    return x*y

#이것을 람다로하면

lambda x, y : x*y  #특징은 함수의 이름이없다
#그래서 람다를 쓸떄는
# a = lambda~ 식으로 함수에 담아서쓴다
# a(x,y) 이런식


lambda_mul_func = lambda x,y:x*y # 변수에 람다 할당완료
print(lambda_mul_func(20,50)) # 바로 변수로사용

def func_final(x,y,func):  # 정해지지않은 펑션을 넣고
    print(x*y*func(100,100))
func_final(10,20,lambda x,y:x*y) #람다로 즉각 함수형성
