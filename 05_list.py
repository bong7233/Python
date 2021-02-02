# chapter03-03
# 파이썬 ㅣ스트
# 자료구조에서 중요
# 리스트 자료형( 순서가있고 중복도가능 수정도가능 삭제도가능한 유일한 자료형)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
print(len(c))
d = [1000, 10000, 'ace', 'base', 'captine']
e = [1000, 10000, ['ace', 'base', 'captine']]
f = [21.42, 'food', 3, 4, False, 3.1411]

# 인덱싱 = 원하는 데이터를 꺼내오는 과정

print('d -', type(d), d)
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e -', e[-1][1])
print('e -', list(e[-1][1])) # 중요중요 타값이든 list()를 사용해 리스트로변경가능

# 슬라이싱
print('d -', d[0:3])
print('d -', d[2:])
print('e -', e[-1][1:3])

# 리스트 연산
print('c + d', c + d) # 리스트+리스트=리스트
print('c * 3' , c * 3)
print("'Test' + 'c[0]'", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])

# identity
# 리스트도 하나의 주소값을 공유할 수 있음을 기억
temp = c
print(temp,c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
c[0] = 4
print('c -', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']] 넣으면 리스트가들어감
print('c -', c)
# 슬라이싱 범위를 정해줬을때는 하나의 원소로들어감
c[1] = ['a', 'b', 'c']
print('c -', c)
# 슬라이싱 자리만 정했을때는 하나의 리스트로 중첩되어들어감
# 중쳡 = 리스트안에 리스트가 들어가는것

c[1:3] = []
print('c- ', c)

del c[2] # 삭제
print('c -', c)
print()
################################################
#리스트 함수
a = [5, 2, 3, 1, 4]

print('a -', a)
a.append(10) # 리스트의 끝에 데이터 추가
print('a -', a)
a.sort() # 오름차순
print('a -', a)
a.reverse() # 반대로
print('a -', a)
print('a -', a.index(3), a[3])
a.insert(2, 7) # 추가할 위치,값 으로 삽입
print('a -', a)
a.reverse()
print('a -', a)

# del은 인덱스위치를 알아야하므로 remove함수 사용이 빠르고좋음
a.remove(10)
print('a -', a)
print('a -', a.pop()) # pop = 리스트의 마지막 인덱스를 꺼내옴(잘라내기)
print('a -', a)
# pop()에 위치를 넣어서도 삭제가능한듯하다, ()의 뜻이 마지막을뜻하는건가?
print('a -', a.count(4)) # count = 값이 몇개나있나

ex = [8, 9]
a.extend(ex)
print('a -', a)

# 반복문 활용
while a:
    data = a.pop()
    print(data)
