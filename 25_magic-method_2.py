# 매직메소드 심화
# 백터 / 크기와 방향을갖는 값 백터의 연산에대해 숙지.

class Vector(object):
    def __init__(self, *args):
        '''
        백터 생성, 예: v= Vector(5,10)
        '''
        if len(arg) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = arg

    def __repr__(self):
        '''
        백터에대한 정보호출
        '''
        return 'Vector(%r,%r)' % (self._x, self._y)

    def __add__(self, other):
        '''백터의 덧샘'''
        return Vector(self._x+other._x, self._y+other._y)

    def __mul__(self, y):
        return Vector(self._x *y, self._y *y)

    def __bool__(self):
        '''좌표에서 0,0이면 false 반환'''
        return bool(max(self._x, self._y))

# 함수에대한 설명을 보려면?
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

# Vector 인스턴스 생성
v1= Vector(5,6)
v2= Vector(20,50)
# init 에서 조건문을 주었으므로 오류생성되지 않음
v3= Vector()

print(v1+v2+v3)
print(v1*3)
print(bool(v1), bool(v2), bool(v3))