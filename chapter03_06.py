# chapter03_06
# 집합
# Set = 자료형 (순서x, 중복x, 수정o)

# 선언
a = set()
print(type(a))
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'pen', 'cap', 'plate'])
e = {'foo', 'bar', 'baz', 'fps', 'qux'} # key없는 소괄호의 자료형들집합은 set
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a -', type(a), a, 2 in a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)
print('e -', type(e), e)
print('f -', type(f), f)

# 튜플 변환(set ->tuple)
t = tuple(b)
print('t -', type(t), t)
print('t -', t[0], t[1:3])

# list 변환(set -> list)
l = list(c)
l2 = list(e)

print('l -', l)
print('l2 -', l2)


# len
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 :', s1 & s2)
print('s1 & s2 :', s1.intersection(s2)) # s2와의 교집합
print(type(s1.intersection(s2)))
print('s1 | s2 :', s1 | s2)
print('s1 | s2 :', s1.union(s2)) # s2와의 합집합

print('s1 -s2 :', s1 - s2)
print('s1 -s2 :', s1.difference(s2)) # s2와의 차집합

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) # false = 교집합있다 True=교집합없다 혼동주의

# 부분 집합 확인
print(s1.issubset(s2)) # false= 아니다
print(s1.issuperset(s2)) # s1이 s2를 포함하나

# 추가 & 제거
s1 = set([1, 2, 3, 4])
# append,insert 등이있었지만, set에서는 add라는정해진 추가매소드가잇음
s1.add(5)      # 추가
print('s1 -', s1)
s1.remove(2)   # 제거 but 제거할 요소가없으면 error 발생함
print('s1 -', s1)
s1.discard(9)  # 제거 but 제거할 요소가 없어도 정상작동
print('s1 -', s1)
s1.clear()  #  싹 다지움
print('s1 -', s1)
