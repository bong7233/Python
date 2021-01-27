# chapter04_02
# For 반복문

# for in <집합의모음(튜플 리스트 딕셔너리 등등)>:
#       (반복문) 형식

for v1 in range(10): # 0부터시작해서 9까지
    print('v1 is :', v1)

for v2 in range(1, 11): # 1부터 10까지
    print('v2 is', v2)

for v3 in range(1, 11, 2): # 1부터 10까지중 2단위로
    print('v3 is', v3)

# 1~1000 합

sum1 = 0

for v in range(1, 1001):
    sum1 += v
#  sum 함수로 했더라도 디버깅과정에서는 for반복문을통해 검사하는것도 가능
print('1 ~ 1000 sum : ' , sum1)

print()

print('1 ~ 1000 sum: ' , sum(range(1, 1001))) # sum 함수자체의 기능으로 쉽게가능
# range(a,b) ab가 정수라면 정수의 list를 만들어줌
print('1 ~ 1000 4 :', sum(range(1, 1001, 4)))

# Iterables = 반복할수 있는 객체 -> __iter__ 인듯
# string, list, tuple, set, dict 가능
# iterable return funtion : range, reversed, enumerate, filter, map, zip

# 리스트 가능

names = ['Lee', 'Park', 'Cap', 'Kim']

for name in names:
    print('You are :', name)

lotto = [11, 19, 21, 28 ,36]

for n in lotto:
    print('Num :', n)

# 문자열 가능
word = "beautiful"

for s in word:
    print('word :', s)

# dict 가능
my_info = {
    "name" : 'Lee',
    "Age" : 30,
    "City" : 'San'
}

for k in my_info: # dict 반복시 value가 아닌 key를 반복함//
    print('key:', k) # value를 하려면 k 대신 my_info[k]
    print('value:', my_info.get(k)) # get 메소드를 사용해도 쉽게가능###

for v in my_info.values(): # value 메소드로 더 간단하게 가능 #####best
    print('value:', v)

##############################################################

# if 와 for 문을 같이 사용해보기

name = 'FineaPplE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
# 메소드에대해 외울 필요가있을듯

# break = 뒷부분은 실행되지 X
# 알고리즘에서의 순차검색 ( 리스트에서 원하는 자료를 찾기위해 n번 다 수행)
# 불필요한 뒷부분 과정을 생략하여 메모리 절약가능
numbers = [14, 3, 4, 7, 10, 24, 4, 1, 11, 34]

for num in numbers:
    if num == 4:
        print('Found: 4!')
        break
    else:
        print('Not found :', num)

# continue  :  반복문을 멈추지않고 다시 출발선

lt = ["1", 2, 5, True, 4.1, complex(4)]

for v in lt:
    if type(v) is bool:# 자료형을 비교할때는 is를 사용 ///
        continue
    print("current type:",v , type(v))

## break 와 continue 사용에대해 고민해보


# for -else

numbers = [14, 3, 4, 7, 10, 24, 4, 1, 11, 34]

for num in numbers:
    if num == 24:
        print("Found : 24")
        break
else:
    print('Not found:24')

    # -->> for 문에서 break를만나 종료되면 else는 실행되지 X

# 연습해보기 reverse

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i *j), end='')
    print()

# 변환

nick = 'Bongman'

print('Reversed', reversed(nick)) # id 값이나옴 ;
print('List', list(reversed(nick)))
print('tuple', tuple(reversed(nick)))
print('Set', set(reversed(nick))) # 순서없음 set의 특징
