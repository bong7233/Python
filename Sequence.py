# 시퀀스형은 쉽게말해 순서가있다고 생각하면됨
# 파이썬에서는 데이터를 두종류로나눔
# 컨테이너 자료형(Container : 서로다른 자료형을 담는것[list,tuple,collections.deque])
# 플랫(Flat : 한개의 자료형만 담는것[str, bytes, bytearray, array.array, memoryview])
# 가변형(list, bytearray, array.array, memoryview, deque)
# 불변형(tuple, str, bytes)


# 지능형 리스트(Comprehending list)

chars = '+_)(*&^%$@!' # Flat형이면서 불변형
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1) # [43,95,41,40,42,38...]

# 지능형리스트로 해보면? list comprehension을쓰면 속도가 빠름
code_list1 = [ord(s) for s in chars]


# 지능형리스트에 map,filter까지 더한다면?
# filter 는 원하는 조건으로 뽑아올수있음
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

print(code_list3) # 40미만의 유니코드만 나옴
print(code_list4) # 값은 똑같이나옴

# 유니코트를 문자열로 다시출력해보면
print([chr(s) for s in code_list1]) # 기호를 리스트에 넣어서 출력됨


# 제네레이터 생성해보기
# 파이썬의 제네레이너 : 시퀀스를 생성해내고, 이터레이터다
# 이터레이터 ? __iter__   
# array는 플랫,가변형
# a = [1,2,3,4....9999] 식으로 할당하면 메모리를 엄청차지함..
# 만약 제네레이터를 쓰면? 1쓰고나면 지우고 2저장, 2쓰고나면 지우고3저장 이런식이라 메모리 효율이좋음
# 파이썬 제네레이터 찾아서 더 공부하기

# Generator : 한번에 한개의 항목을 생성(메모리유지하지않음)
import array

# list comprehesion 형태에서 밖을 소괄호로 묶으면 제네레이터로 됨
# 이때는 메모리에 입력하기전에 가지고만있는상태
tuple_g = (ord(s) for s in chars)
print(next(tuple_g)) # 하면 하나씩하나씩만 프린트됨

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
# 물결3개들어있는 4개의 리스트를 만듬

marks2 = [['~'] * 3 ] * 4
# 프린트하면 결과는 mark1과 같음

# 수정해보기
marks1[0][1] = 'x' # 하면 첫번째 리스트의 1인덱스만 변경됨
marks2[0][1] = 'x' # 하면 모든리스트의 1인덱스가 다 바껴버림(의도치않음)

# why? marks1은 4개의 리스트가 모두 다른 id값을 가지지만,
# marks2는 4개의리스트가 모두 같은 id값을가짐(하나의 리스트를 통쨰로*4해버려서..)

##########################################


# Tuple Advance
# Unpacking

# b, a = a, b 이것도 언패킹이다(파이썬이니까 간단하게 가능한것)

print(divmod(100,9)) # 100을 9로나눈 몫과 나머지 (11,1) 반환
print(divmod(*(100,9))) # *로 언패킹해서 넣음
print(*(divmod(100,9))) # 결과값자체를 언패킹 11 1  반환


# *를 이용해 언패킹하는예시 / 파이썬의 장점중하나
x, y, *rest = range(10)
print(x,y,rest) # 0 1 [2,3,4,5,6,7,8,9]

x, y ,*rest = range(2)
print(x,y,rest) # 0 1 []

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest) # 1 2 [3,4,5]

#



