# chapter04_01
# 제어문
# IF

# 기본형식
print(type(True)) # 0이 아닌 수, 문자, 데이터가있는 리스트
print(type(False)) # 0, 빈문장, 데이터가없는 리스트형


# ex
if True:
    print('good')

if False:
    print('bad')

if False:
    print('bad')
else:
    print('good')

# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)

city = ''
if city:
    print("You are in:", city)
else:
    print("Please enter your city")

# 논리연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and:', a > b and b > c)
print('or:', a > b or b > c)
print('not:', not a > b)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1:', 3+12 > 7+3)
print('e2:', 15*3 > 10*20)
print('e3:', 5+10 > 3 and 7+3 ==10)
print('e4:', True and not True)

score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참이여야 실행
if score1 >= 90 and score2 == 'A':
    print('PASS')
else:
    print('FAIL')

# 연습
id1 = 'vip'
id2 = 'admin'
grade = 'gold'

if id1 == 'vip' or id2 == 'admin':
    print('admin')

if id2 == 'admin' and grade == 'gold':
    print('sudo')

# 다중 조건문

num = 90

if num >= 90:
    print('Grade :A')
elif num >= 80:
    print('Grade :B')
else:
    print('FAIL')

# 중첩 조건문 IF 안에 IF
# 너무많은 중첩조건문은 금지
grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print('Upgrade')
    elif total >= 80:
        print('Stay')
    else:
        print('Downgrade')
else:
    print('In next life')

# in, not in

q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {"name": "Lee", "City": "san"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("san" in e.values()) # 그냥 san은 key가아닌 value기떄문에 메소드써야댐
