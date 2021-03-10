# 파일 입출력

# 읽기 r , 쓰기 w , 추가 a , 텍스트모드 t , 바이너리모드 b
# 상대경로(' ../ . ') 절대경로('C:\Django\example..')
# 상대경로는 지금파일기준으로, 바로 사용가능
# 하지만 하나이상의 환경에서작업하면 절대경로가 다 다를수있어서 조심

# Read
# 절대경로보다 상대경로가 더쉽다.
f = open('./resource/it_news.txt', 'r', encoding='utf-8')

print(dir(f)) # 파일과 연결된상태에서 쓸수있는 메소드들이 나옴

print(f.encoding) # 인코딩 확인 지금경우는 utf-8
print(f.name) # 이름확인
print(f.mode) # 모드확인 지금은 read
cts = f.read()
print(cts) # 내용읽음
f.close() # 닫기 / 안닫아도 운좋게 에러가안날수있지만...나중에큰일남

### with 사용하기 ###
with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
    c = f.read()
    print(c)
    print(iter(c)) # iter로 오브잭트 레퍼런스가나오면 반복사용가능함을뜻함
    print(list(c))

print()

# read() = 전체읽기 / read(10) = 10바이트만큼만 read함
with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
# 이과정을하면 처음부터가아니라 처음과정의 끝부터 시작함.
# 즉 커서가 있음을 알 수 있음
# 이때 f.seek(0,0) 을 하면 처음으로 돌아가서 출력함

# readline : 한줄씩 읽기 ( \n 을 만날때까지)
with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

# readlines : 전체를 읽은 후 라인단위 리스트 저장
with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
    ctf = f.readlines()
    print(ctf)
    for c in ctf:
        print(c, end='')


### Write ###
with open('./resource/contents.txt', 'w') as f:
    f.write('I Love cat\n')
# append는 본문 뒤에 삽입
with open('./resource/contents.txt', 'a') as f:
    f.write('I Love cat\n')

# Writelines : 리스트 -> 파일로
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'apple\n']
    f.writelines(list)

# print뒤에 file=f 를 쓰면 콘솔에서 뜨는게아니라 파일에 입력이된다.특이함
with open('./resource/contents3.txt', 'w') as f:
    print('Cat cat cat want cat', file=f)
