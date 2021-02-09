# 분할된 개별적인 모듈이 뭉친폴더가 패키지다.
# sub라는 패키지를 다운받앗음
# 파이썬은 패키지로 분할된 개별적 모듈로 구성
# ..은 부모디렉토리로, .은 현재디렉토리 -> 모듈 내에서만 사용
# __init__.py: python 3.3 부터는 없어도 패키지로인식
# 하지만 하위호환을위해 작성해두는것.


# 예제1
import sub.sub1.module1 # 같은경로에있을때는 바로 찾아갈수있음
import sub.sub2.module2

# 사용

sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

#바로전에배운 sys.path를이용한다면
#이 경우처럼 sub 파일을 다운받아서 위치할 필요없다

# 예제2 / 예제1처럼할경우 길이가 길어지면 비효율적
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # alias(별명)

module1.mod1_test1()

m2.mod2_test1()

# 예제3
from sub.sub1 import *  # *(asta )로 가져오면 하위의 모든파일 접근가능
from sub.sub2 import *

module1.mod1_test1()
module2.mod2_test1()    # 다가능 . 하지만 메모리를위해
                       # asta는 왠만하면 사용하지않음
# 이런 작업을할떄마다 pycache 파일생기는데
#그냥 지워도 무관함
