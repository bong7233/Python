# Chapter04_03
# While 반복문
# for와는 다르고 if문과 비슷한성격

# While <expression>: expression의 조건을 만족하는한 계속 반복
#   <statement(s)>
n = 5
while n > 0:     # while = True 는 무한반복/ 사용하지않는게 안전
    n = n - 1
    print(n)

print()


a = ['abc', 'def', 'ghi']

while a:          # a 자체가 존재하는 true 즉 1이므로 무한
    print(a.pop())

#############################
#break , continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')

# if 중첩
# while은 break문과 자주 쓰이기 때문에 if문이 중첩되어 들어가는 경우가많음
i = 1

while i <= 10:
    print('i:',i)
    if i == 6:
        break
    i += 1

# while else

n = 10

while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out') # break로인해 마무리되어 else문 실행되지 X

#############################################################
a = ['bong', 'sang', 'lee', 'man']
s = 'yeah'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list')

# 무한루프조심

a = ['bong', 'man', 'hhhh']

while True:   # while true 패턴에 조건문넣는식도 많이활용됨 고민해보기
    if not a:
        break
    print(a.pop())
