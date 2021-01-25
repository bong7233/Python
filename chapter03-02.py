# Chapter03-02
# 파이썬 문자형

# 문자열 생성
str1 = "I am Bong"
str2 = "Bong"
str3 = """BONG?"""

print(type(str1), type(str2), type(str3))
print(len(str1))

# 빈 문자열 표현법
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), type(str1_t1))
print(type(str2_t2), type(str2_t2))


# 이스케이프 문자 사용
# I'm BONG
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""

print("I'm bong") #내부에 ' 와 "의 유무 주의
print('I\'m bong') # \뒤의 기호는 그대로출력

print('a \t b')
print('a \"\"b')

escape_str1 = "Do you like \"FPS\" ?"
print(escape_str1)

# 탭, 줄 바꿈
t_s1 = "Click \t Start"
t_s2 = "New Line \n Check"

print(t_s1)
print(t_s2)
print()


# Raw string 출력
raw_s1 = r'D:\python\test'
print(raw_s1)

# 멀티라인 입력 \사용
multi_str =\
'''
string
multi Line
test
'''

print(multi_str)

# 문자열 연산 (파이썬이라 가능)
# 시퀀스에 속하는 타입은 모두 연산가능
str_o1 = "bong"
str_o2 = "dong"
str_o3 = "workout every day"
str_o4 = "Came from JJ"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('b' in str_o1)
print('p' not in str_o1)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

#문자열 함수(upper, isalnum, startswith, count, endswith isalpha...)
print("Capitalize: ", str_o1.capitalize()) #첫글자 대문자로
print("endswith?: ", str_o2.endswith("!")) #변수의 끝에 !가 있나?
print("replace", str_o1.replace("ong", 'good'))
print("sorted: ", sorted(str_o1)) # 정렬, 후에 다시보기
print("split: ", str_o4.split('s')) #s를 기준으로 리스트형태로 분리배열

# 반복(시퀀스)
im_str = "Good Bong!"

print(dir(im_str)) # dir에 넣어서 __iter__ 가 있다면 시퀀스가 가능하다

# 출력
for i in im_str:
    print(i)

# 슬라이싱 연습  ****굉장히 중요****
str_s1 = "Nice Bong"

print(str_s1[0:3])
print(str_s1[5:10])
print(str_s1[5:]) #빈자리 = 끝까지
print(str_s1[:len(str_s1)]) # =str_s1[:11]
print(str_s1[1:6:2]) # 1부터 4까지 가져오되 2칸단위로
print(str_s1[-4:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

# 아스키 코드(or 유니코드)
a = 'z'
b = 'Z'
print(ord(a))
print(ord(b))
print(chr(122))
