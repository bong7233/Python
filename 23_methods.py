# 다양한 메소드들과 개념정리하기

class Car:
# 내가 지정한 것에대한 요약을 적음
    """
    Car class
    Author : Bong
    Date : 2021-02-23
    Description : Class, Static, Instance Method
    """

    #클래스변수(모든인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company # 인스턴스변수
        self._details = details

    # 사용자입장에서의 프린트문으로 보기
    def __str__(self):
        return 'str : {}'.format(self._company,self._details)

    # 개발자입장에서 객체의 엄격한 타입을 문자열로볼때
    def __repr__(self):
        return 'repr : {}'.format(self._company,self._details)
    # 하지만 str이 없고 repr만 있으면 repr을 str로 인식해서 표시함

    # Instance Method
    # self  : 객체의 고유값을 사용
    def detail_info(self):
        print('Current ID:{}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._detail.get('price')))

    # Instance Method (self를 받는다)
    def get_price(self):
        return 'Before Car Pirce -> company:{}, price:{}'.format(self._company, self._details.get('price'))

    # Instance Method
    def after_price(self):
        return 'After Car Pirce -> company:{}, price:{}'.format(self._company, self._details.get('price')*Car.price_per_raise)

    # Class Method (cls를 받는다)
    @classmethod
    def raise_price(cls,per):
        if per <= 1:
            print('Enter 1 or more')
            return
        else:
            cls.price_per_raise = per
            return 'Succeed!'

    # Static Method (아무것도 안받으며 유연하게 클래스든 인스턴스든 사용할수있다.)
    # 자주쓰이진않지만 클래스나 인스턴스에 넣기 애매하면 활용(하지만 이 함수에 한해서사용)
    @staticmethod
    def is_bmw(inst): # 여기서 inst는 그냥 내가정하면된다 일반적인 함수처럼
        if inst._company == 'BMW':
            return 'Yeah, that is BMW'
        else:
            return 'No...'

car1 = Car('Ferrari', {'color':'white','horse':400,'price':7000})
car2 = Car('BMW', {'color':'black','horse':500,'price':8000})

# 가격에 직접 접근하는것보다 메소드로 만들어서 뽑는게좋음
print(car1.get_price())

# 가격인상
Car.raise_price(4)
print(car1.after_price())

# 스테틱메소드 써보기
print(car1.is_bmw(car1)) # 인스턴스로호출
print(Car.is_bmw(car1)) # 클래스로호출  // 둘다 가능하군
