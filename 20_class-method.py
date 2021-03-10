# 절차지향 객체지향 차이 완벽하게구분하기
# 객체지향(OOP) 장점 클래스기반 코딩해보기
# 큰 규모 project에서 함수중심프로그래밍 -> 데이터방대해지므로 복잡해짐
# 그래서 클래스중심으로 코딩-> 데이터가 중심이고 구성요소들이 객체로써관리
# 즉 중복방지, 재사용가능, 대형프로젝트의 유지보수편리
# 간단한 과정에는 당연히 함수중심으로 짜는게 쉽고 빠름

# 일반적코딩 = 요소마다 추가
# 100개면 100번추가

# 리스트구조 (인덱스로 접근가능하다는 이점)
# but 각각의 리스트를 일일이 관리, 인덱스,삭제도 위치알아야해서 불편


class Car:
# 내가 지정한 것에대한 요약을 적음
    """
    Car class
    Author : Bong
    Date : 2021-02-23
    기타등
    """

    #클래스변수(모든인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self.company = company # 인스턴스변수
        self.details = details
        Car.car_count += 1
    # 사용자입장에서의 프린트문으로 보기
    def __str__(self):
        return 'str : {}'.format(self.company,self.details)

    # 개발자입장에서 객체의 엄격한 타입을 문자열로볼때
    def __repr__(self):
        return 'repr : {}'.format(self.company,self.details)
    # 하지만 str이 없고 repr만 있으면 repr을 str로 인식해서 표시함

    def detail_info(self):
        print('Current ID:{}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self.company, self.details))

    def __del__(self):
        Car.car_count -= 1
# 각각의 instance는 다른 id값과 내용을 가지고있음을 기억
car1 = Car('Ferrari', {'color':'white','horse':400,'price':7000})
car2 = Car('BMW', {'color':'black','horse':500,'price':8000})
car3 = Car('Audi', {'color':'yellow','horse':300,'price':4000})

# Doctring (클래스밑에 """로 적은 내용이 보임)
print(Car.__doc__)

print(car1.detail_info())

Car.detail_info(car1)

del car1
print(Car.car_count)
# 만약 인스턴스변수를 _로 시작해놓으면
# 이결과값을보고 어떤게 인스턴스변수인지 클래스변수인지 쉽게 구분할슀다.
print(dir(car2))

# 인스턴스 네임스페이스에없으면 -> 클래스에서 검색
# 한마디로 인스턴스에 오버라이드 가능하다~
