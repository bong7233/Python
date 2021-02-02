# Chapter02-2
# 파이썬 변수

#기본선언
n = 700

print(n * 700)
print(type(n))

#동시선언
x = y = z = 700
print (x, y, z)

# 선언
var = 75

# 재선언
var = "change"

#출력
print(var)
print(type(var))

# object References
# 변수 값 할당 상태
# 1.타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n =777

print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 600

print(id(m))
print(id(n))
print(id(m) == id(n))

m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
