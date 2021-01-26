# Chapter03_05
# Dictionary
# 범용성높음
# dic (순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name': 'Lee', 'phone': '46697233', 'birth': '0121'}
# 키중복x = name이 두개면 안된다는것
# 키는 어떠한 자료형으로도 가능 보통 문자형씀
b = {0: 'hello'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'bong',
    'City': 'san',
    'Age': 30
}

# 이렇게 dict(리스트(튜플)) 형태로 가끔 쓰기도함
e = dict([
    ('Name', 'bong'),
    ('City', 'san'),
    ('Age', 30)
])

# 간단하고 가독성 높음
f = dict(
    name='bong',
    city='san',
    age= 30
)

print('a -', type(a),a)
print('b -', type(b),b)
print('c -', type(c),c)
print('d -', type(d),d)
print('e -', type(e),e)
print('f -', type(f),f)

# 출력
print('a -', a['name']) # []사용시 키 없으면 error
print('a -', a.get('name1')) #get 사용시 키 없으면 none 으로뜸
print('b -', b[0])
print('b -', b.get(0))
print('f -', f.get('city'))

# 딕셔너리 추가
a['address'] = 'bondong'
print('a -', a)
a['rank'] = [1, 2, 3]
print('a -', a)

# dick 에서의 len 은 키의 갯수를 세는것
print('a -', len(a))

# dict_keys, dict_values, dict_items : 반복문에서 사용 가능
print('a -', a.keys())
print('b -', b.keys())
print('c -', c.keys())
print('a -', list(a.keys())) #키를 리스트로 정리가능
print()

print('a -', a.values())
print('a -', list(a.values()))

print('a -', a.items())
print('b -', b.items())

print('a -', list(a.items())) # 키와 내용을 퓨틀로 리스트함

print()

print('a -', a.pop('name')) # 똑같이 꺼내오기가능
print('a -', a)

print()

print('f -', f.popitem()) # pop()는 임의의 하나를 빼옴 , 딕셔너리는 순서가 없기때문
print('f -', f)

print()

print('a -', 'birth' in a)
print('a -', 'Birth' in a) # key 의 대소문자 중요
print('a -', 'hobby' in b)

# 수정 & 추가를 속성값으로 바로 가능
a['test'] = 'test_dict'
print('a- ', a)

# update라는 메소드
a.update(birth='920121')
print('a-', a)

# 명시적으로 특정 리스트를  사용하여 업데이트도 가능
temp = {'address': 'sanbon'}
a.update(temp)
print('a-', a)
