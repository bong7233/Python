# module
# 완성된 코딩 덩어리(변수,클래스,함수들) 파일.
# 평소 쓰던 import 뒤의 re, random, math 등등이 해당된다.

def add(x, y):
    return x + y

def sbubtract(x, y):
    return x - y

# 이런식으로 유용한 함수들을 만들어서 저장해둠
# 예를들어 mymath  로 저장해두고, 다른곳에서 import mymath 하면 x.add 로 바로사용가능

# 이미 설치된 모듈들의 위치를 보려면
import sys                      # 예로 sys 모듈
print(sys.path)

# 만약 다른모듈을 가져와서 사용하려면 append 로 떙겨와서 사용가능
mymath.path.append('파일위치')  # ex) C:/mymath

# 모듈 생성시 실험을위한 과정 ( 예를들어 print문) 등을 사용자에게 불필요하게 보여지지않게

if __name__ == "__main__":  # 식으로 모듈내에서 실험해볼수있고,
    print('블라블라')       # 모듈을 받아서 사용하는사람도 이 내용을 예시로 이해할수있음.


