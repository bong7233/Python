# 논리적으로 이해먼저해야할듯
# 파이썬 내장함수 (Built-in)
# 자주 사용해서 외우는게중요
# 함수만 따로 다 외운다고해서 다외워지지않음

# 절대값 = abs()
print(abs(-3)) # 3

# all : iterable 요소 검사(참,거짓)
print(all([1,2,3])) # 요소가 하나라도 False 면 False 반환

# any
print(any([1,2,0])) # 요소가 하나라도 True 면 True 반환

#  chr : 아스키코드->문자 / ord : 문자->아스키코드
print(chr(76))
print(ord('f'))

# enumerate : 인덱스 + Iterable(반복가능한 list tuple 등등) 객체 생성
for i, name in enumerate(['ab','bc','cd']):
    print(i,name)

# filter : 반복가능한 객체요소를 지정한 함수조건에 맞는값만 추출
# 데이터 전처리시 , 크롤링해온 데이터를 처리시 자주쓰임
def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 5, 6])))
# 람다로 해보자면
print(list(filter(lambda x: abs(x) > 2, [1,-3,2,5,6])))

# id : 객체의 레퍼런스(주소)를 반환
print(id(int(5)))
print(id(4))

# len : 길이반환
print(len('abababab'))
print(len([1,2,3,4,5,6]))

# max , min : 최대값, 최소값
print(max([1,2,3,4,5]))
print(max('python'))  # 알파벳순으로 오름차순해서 높은알파벳
print(min('python good')) # 공백이있을땐공백이 가장낮은걸로 인식

# map : Iterable한 객체요소를 지정한함수실행후 추출
def conv_abs(x):
    return abs(x)
print(list(map(conv_abs,[1,2,3,4,5,6])))
# 이것도 람다로바꿔보면
print(list(map(lambda x:abs(x),[1,2,3,4,5,6])))

# pow : 제곱값 반환
print(pow(2,10))

# range : 반복가능한 객체 반환
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

# round : 반올림
print(round(6.5111, 2)) # 2자리수까지 반올림해라
print(round(5.6)) # 자리수 안정해주면 바로 첫쨰자리 반올림
print(round(5.66)) # 뒤에 2자리여도 그냥 첫쨰로함

# sorted : 반복가능한객체 Iterable=( list tuple set dic) 네개는 꼭 마스터
#          를 오름차순
print(sorted([1,5,2,3,6,7]))
print(sorted(['p','w','q','r']))
# key 값을 활용해서 key기준 정렬도가능함/ sorted관련해서 찾아보기

# sum : Iterable 객체 합 반환
print(sum(range(1,10)))

# type : 자료형 확인
print(type(3))
print(type({}))
print(type((1,)))

# zip : 반복가능한 Iterable객체 묶어서반환

print(list(zip([1,2,3],[4,5,6])))
# 짝이 맞지않으면 맞는것만 반환함
print(type(list(zip([1,2,3],[4,5,6]))[0])) # 각각은 튜플로반환
# 즉 튜플이 들어있는 리스트형태로 나옴
