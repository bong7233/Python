# 기존 파이썬의 리스트 = 변경가능한 유연한 자료형
# 시퀀스형은 쉽게말해 순서가있다고 생각하면됨

# 파이썬에서는 데이터를 두종류로나눔
# 1. 컨테이너 자료형 (Container : 서로다른 자료형을 담는것[list,tuple,collections.deque])
# 2. 플랫 (Flat : 한개의 자료형만 담는것[str, bytes, bytearray, array.array, memoryview])
# 플랫형이 굳이필요할까? -> 대용량의 데이터를 처리할떄 조금이라도 메모리와 시간을 절약하기위해
# 언젠가 꼭 필요한 자료형이 플랫

# 가변형(list, bytearray, array.array, memoryview, deque) - 수정가능
# 불변형(tuple, str, bytes) - 수정불가능

# 컨테이너 자료형? 여러개의 자료형을 한번에담음
a = [3, 's', 3.0]

# 플랫자료형? 같은자료형을 한번에 담음
b = [3, 4, 10]


# 리스트 및 튜플의 고급형태

## 지능형 리스트(Comprehending list)
chars = '+_)(*&^%$@!' # Flat형이면서 불변형(str이므로)
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

# ord() 각 요소의 유니코드 번호 출력
# 하나하나가 순서대로 출력되는것을 확인가능
print(code_list1) # [43,95,41,40,42,38...]

## 지능형리스트로 해보면? list comprehension 사용
code_list1 = [ord(s) for s in chars]

## 지능형리스트(comprehending)에 map,filter까지 더한다면?
## filter 는 원하는 조건으로 뽑아올수있음
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

print(code_list3) # 40미만의 유니코드만 나옴
print(code_list4) # 값은 똑같이나옴

# 유니코트를 문자열로 다시출력해보면
print([chr(s) for s in code_list1]) # 기호를 리스트에 넣어서 출력됨


# 제네레이터 생성해보기 (제너레이터는 파이썬에서 매우중요)
# 파이썬의 제네레이너 : 시퀀스를 생성해내고, 이터레이터다
# 이터레이터 ? dir() 속성안에 있는 __iter__ (연속적인 for문 등에서 사용가능하다)
# 위치를 기억하고있다가 다음에 사용할떄 위치로 바로 불러올수있다,반복할수있다
# array는 플랫,가변형
# a = [1,2,3,4....9999] 식으로 할당하면 메모리를 엄청차지함..
# 만약 제네레이터를 쓰면?
# 1쓰고나면 지우고 2저장, 2쓰고나면 지우고3저장 이런식이라 메모리 효율이좋음

# Generator : 한번에 한개의 항목을 생성(메모리 유지하지 않음)
import array

# 이때는 메모리에 입력하기전에 가지고만있는상태
tuple_g = (ord(s) for s in chars)
print(tuple_g) # 하면 값이나오는게아니라 generator 객체가 나옴
print(type(tuple_g)) # type generator

 # 하나씩하나씩만 프린트됨
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

# array.array = np.arry와 비슷하다, 수치연산에 특화되어있다
array_g = array.array('I', (ord(s) for s in chars))
print(array_g.tolist()) # 하면 array를 list로 출력해줌


# 제네레이터 실습해보기
print(('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21)))

for s in ('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21)):
    print(s)
    # 하나하나 만들어서 프린트함


######## 리스트사용할때 주의할점 ( 깊은복사, 얕은복사) #######
# 매우중요

marks1 = [['~'] *3 for n in range(4)]
# [['~','~','~'], ['~','~','~'], ['~','~','~']]
# 물결3개들어있는 4개의 리스트를 만듬

marks2 = [['~'] * 3 ] * 4
# [['~','~','~'], ['~','~','~'], ['~','~','~']]
# 프린트하면 결과는 mark1과 같음

# 수정해보기
marks1[0][1] = 'x' # 하면 첫번째 리스트의 1인덱스만 변경됨
# [['~','X','~'], ['~','~','~'], ['~','~','~']]

marks2[0][1] = 'x' # 하면 모든리스트의 1인덱스가 다 바껴버림(의도치않음)
# [['~','X','~'], ['~','X','~'], ['~','X','~']]


# why? marks1은 4개의 리스트가 모두 다른 id값을 가지지만,
# marks2는 4개의리스트가 모두 같은 id값을가짐(하나의 리스트를 통쨰로*4해버려서..)

##########################################


# Tuple Advance
# Unpacking

# b, a = a, b 이것도 언패킹이다(파이썬이니까 간단하게 가능한것)
# 다른 언어에서는 교차함수를 사용하여 일일이 바꿔주는 과정이 필요

print(divmod(100,9)) # 100을 9로나눈 몫과 나머지 (11,1) 반환
print(divmod(*(100,9))) # *를 앞에붙이면 언패킹 가능 (11,1)
print(*(divmod(100,9))) # 결과값자체를 언패킹 11 1  반환


# *를 이용해 언패킹하는예시 / 파이썬의 장점중하나
x, y, *rest = range(10)
print(x,y,rest) # 0 1 [2,3,4,5,6,7,8,9]

x, y ,*rest = range(2)
print(x,y,rest) # 0 1 []

# 그냥 선언하면 튜플이지만, *rest로 묶으면 리스트로 묶여서 출력되는것을 기억
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest) # 1 2 [3,4,5]

#############################################

# Mutable  vs   Immutable

l = (15, 20, 25)
m = [15, 20, 25]

l = l * 1
m = m * 2
# 단순 * 연산자를 사용하면 둘다 id값이 바뀜
print(l, id(l))
print(m, id(m))

# *= 연산자 사용시 단순* 사용과는 다른 결과
l *= 2
m *= 2
# 불변형은 재할당시 id값이 바뀐다 (이미 선언된걸 바꿀수없으니 새로할당)
# 가변형은 재할당시 id값이 유지된다 (선언된걸 바꿀수 있으니 덮어씌워버럼)
# 즉 가변형은 연산자의 활용에따라 본체를 추가할수도 따로 만들수도있다
print(l, id(l))
print(m, id(m))

##############################################

# sort   vs   sorted
# reverse, key=len, key=str.lower, key=func ...

# sorted : 정렬 후 새로운 객체 반환 , 원본을 수정하지않음
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# 알파벳 오름차순
print('sorted', sorted(f_list))

# 알파벳 역순
print('sorted', sorted(f_list, reverse=True))

# 글자 길이순으로 정렬
print('sorted', sorted(f_list, key=len))

# 마지막글자를 기준으로 정렬 (lamda로 기준함수를 생성)
print('sorted', sorted(f_list, key=lambda x : x[-1]))

# 마지막글자를 기준으로 역순정렬
print('sorted', sorted(f_list, key=lambda x : x[-1], reverse=True))

print(f_list) # 본체는 위의 과정이 다끝나고 그대로유지됨


# sort : 정렬 후 객체 원본을 변경, 반환하지않음을 기억하자 프린트하면 None 나옴
print('sort', f_list.sort(), f_list) # sort None 바뀐원본
print('sort', f_list.sort(reverse=True), f_list)
print('sort', f_list.sort(key=len), f_list)
print('sort', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
# 전부 원본을 변경시킴


# 그래서 lsit, Array 의 적합한 사용법은?
# 리스트 기반 : 융통성, 다양한 자료형, 범용적사용
# 숫자 기반 : array사용(리스트와 거의 호환됨=리스트에서 사용되는 함수를 array도 사용가능),
# 대부분의 머신러닝러닝에서 array 사용

#############################################

# 해시테이블
# key에 Value를 저장하는 구조(파이썬자체가 강력한 해시테이블엔진으로 이뤄짐)
# key가 중복되지 X, key를 알면 쉽게 value에 직접접근이가능
# Hash 값이 중복되었을떄 어떤 메커니즘으로 처리되는가? 를 정리해두기 (중요)
# 파이썬에서 dictionary 타입이 hashtable의 예라고 보면됨
## key값의 연산결과에따라 직접 value에 접근이 가능한 구조
# key 값을 해싱 함수를통해 -> 해시주소값이 나오고 -> 이걸로 value의 위치를 참조

# 모든값들이 key:value 형태로 되있음을 알 수 있음
print(__builtins__.__dict__)
# {'name: ~~', 'isinstance:~~'} 형태


# Hash 값 확인, "값을 확인할수있다?-> 고유한값이다" 를 기억
t1 = (10,20,(30,40,50))
t2 = (10,20,[30,40,50])

print(hash(t1)) # hash값 나옴, tuple은 불변성이므로 hash값이 변하지 않아서 가능
# (참조값, 식별자같은느낌)

print(hash(t2)) # 에러발생-> list는 가변성이므로 hash값이 변할수 있어서 안됨
# 즉 hash값은 불변형에 한해 가능하다


# Dict Setdefault 예제 (Setdefault는 공식적으로 매우 추천됨)
# 대용량 데이터를 다룰때 속도도 빠름
source = (('k1', 'val1'), # 2중튜플
         ('k1', 'val2'),  # 지금은 딕셔너리가 아닌 그냥 튜플
         ('k2', 'val3'),  # 만약 이대로 그냥사용하면 k1,k2 키값이 중복
         ('k2', 'val4'),
         ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# Setdefault 미사용시
# 결과는 딕셔너리형태로 나옴
for k,v in source:
    # 딕셔너리안에 키가있는지 확인
    if k in new_dict1:
        # 키가 있다면 v를 담아줌
        new_dict1[k].append(v)
    # 키가 없다면 새로운키 만들고 담음
    else:
        new_dict1[k] = [v]

# {'k1':['val1','val2'],'k2':'['val3','val4','val5']}

# Setdefault 사용
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
# {'k1':['val1','val2'],'k2':'['val3','val4','val5']}
# 결과는 똑같이 딕셔너리형태로나옴, 훨씬 간결하고 빠름


### 주의사항 ###
new_dict3 = {k:v for k,v in source}
# # {'k1':'val2','k2':'val5'}
# 이렇게하면 value 값을 나중껄로 덮어씌워버림...

###########################################

# Set 선언시 최적화 방법
