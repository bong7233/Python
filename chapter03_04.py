# 튜플 Tuple
# 리스트와 비교 중요
# 튜플 자료형 (순서o, 중복o, 수정x, 삭제x) 리스트와의 차이점
# 순서와 중복만 가능하고, 수정 삭제가 불가능=불변
# 그래서 한번 설정해서 절대로 변해서는안되는 중요한요소에 사용

# 선언

a = ()
b = (1,)
# 튜플선언시 값이 하나이면 뒤에,를 써주어야 int로 빠지지 않음
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Bong', 'Cap')
e = (100, 1000, ('Ace', 'Bong', 'Cap'))
print(type(a),type(b))

# 인덱싱
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('d -', e[-1])
print('d -', e[-1][1])
# 튜플을 리스트로 변환하면 다시 수정삭제가 가능해짐
print('d -', list(e[-1][1]))

#슬라이싱
print('d -', d[0:3])
print('d -', d[2:])
print('d -', e[2][1:3])

# 튜플 연산
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a -', a)
print('a -', a.index(3))
print('a -', a.count(2))
print()

# packing & Unpacking / 파이썬에서 굉장히 중요한개념

# packing = 묶어놓은어떤요소, 인덱싱이 가능함 ex튜플이나 리스트를 선언하는것
t = ('foo', 'bar', 'baz', 'qux')

# Unpacking = 묶어놓은 요소를 다시 따로뺴내서 요소로 사용
# 이 예제에서는 튜플덩어리를 각각의 str로 빼내어서 사용함
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# pack, Unpacking
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6 # 이 언패킹은 위의 t3을 튜플해서 만들어놔서 가능

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
