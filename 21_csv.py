# CSV = 데이터사이언스에사 많이사용되며, 주로 xml,json,excel 등등
# 어떤 집합을 파일로저장할때 csv 파일로저장하면 다른곳에서 사용하기편리

# CSV : MEME -text/csv

import csv
# 열머릿글(헤더) 에는 관습적으로 자료카테고리가 설정되어있음
# 각각의 자료형이 ,로 구분되어있는게 정석이지만//
# 띄어쓰기나 | 처럼 다른표현으로 구분되어있기도함.

with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # 이렇게하면 한번 리더를 스킵했으므로 첫줄이안나옴
    #왜내면 커서가있으서 첫번쨰줄이 끝나고 두번쨰줄을 기억하고시작함
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 가 있는지 잘보자~

    # __iter__가있으니까 반복문쓸수있다

    for c in reader:
        print(type(c)) # 리스트로 온다는걸 기억
        print(' '.join(c)) # 한칸띄워서 구분지어서 프린트한다
        #print(c)

with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
                    # delimiter 로 원하는 구분기호를 정할수있음
                    # 원래는 , 기준이지만 이렇게하면 | 기준으로 나눔
    for c in reader:
        print(c)


# DictReader에 items메소드를섞어서 세련되게표현가능
# name 과 code 라는 첫줄을 표시해줄수잇으므로 가시성높다
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    print(reader)
    print(type(reader))
    print(dir(reader))  #__iter__ 있음
    print()

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('--------------')


## 새로운 예제
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('./resource/write.csv', 'w', encoding='utf-8') as f:
    print(dir(csv))
    wt = csv.writer(f) # writer라는 메소드로 f를 wt로 쓰는것

    #print(dir(wt))
    #print(type(wt))
    for v in w:
        wt.writerow(v)# writerow로 한리스트씩 구분해서 입력하고
                    # 각각의 줄의 요소들은 ,로 구분되어짐


## key 값을 필드명으로 해서 가져와보기
with open('./resource/write2.csv', 'w', encoding='utf-8') as f:
    #필드명
    fields = ['one', 'two', 'three']
    # dict writer(fieldname이라는 인수의 저정을해주면 fields값이 맞춰서들어감
    wt = csv.DictWriter(f, fieldnames=fields)
    # header writer / 헤더이름으로 넣어주는과정
    # 즉 위에서정한 one two three를 맨윗졸로 올려서 헤드로정함
    wt.writeheader()

    for v in w:
        wt.writerow({'one': v[0], 'two': v[1], 'three': v[2]})
        # 필드명: w안의 각리스트의 순서에맞게 딕셔너리형태로적으면됨
