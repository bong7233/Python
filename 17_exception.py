# 예외처리
# 예외종류
# syntaxError, TypeError, NameError, IndexError, ValueError, KeyError
# 문법적으론 예외없음 but 코드실행단계(프로세스)에서 발생하는예외도 중요
# 1. 예외는 반드시처리해야함
# 2. 로그는 반드시 남겨야함(어떤오류가났었는지)
# 3. 예외는 던져진다.
# 4. 예외 무시도 가능, 좋은방법아님

# syntaxError : 문법오류
# nameError : 참조할것이 없음(주로 변수)
# ZerodivisionError : 100/0 -> 수학적으로 불가능함
# index error : 범위밖을 건드릴때 (특히 알고리즘에서 자주발생)
# KeyError : key없을떄, get메소드로 방지할수있음*

# 일단 작성하고, 실행할때 예외발생시 처리하는것이 권장됨
# 예외까지 생각하고 작성하면 기한내에 절대 처리할수없음 (신입은..)

# AttributeError : 모듈, 클레스에 있는 잘목된 속성 사용
                #  모듈이나 클래스에 존재하지않는 메소드나 함수 호출할떄

# ValueError : 어떤 자료구조안에서 존재하지않는 자료를 참조하려할때

# FileNotFOund Error : 존재하지않는 파일 열때

# typeError : 자료형에 맞지않는 연산을 할때

# 예외처리

# try : 에러가 발생할 가능성 있는 코드 실행
# except 에러명(n개 가능) : 해당에러 발생시 실행
# else : try 블록의 에러가 없을경우 실행
# finally : 항상실행

name = ['kim', 'lee', 'park']

try:
    z = 'kim'
    x = name.index(z)
    print('{} found it! [] in name'.format(z, x+1))
except ValueError:
    print('not found it')
else:
    print('ok!, else')

print('-')
# 정상적으로 예러 예외처리했다면, 이후의 코드도 정상실행

# except (Exception): 으로 모든예외를 포괄적으로 포함할수 있음 Exception 생략가능
# except Exception as e:
#     print(e)         # 로 해당예외를 출력해주면 로그남기기에 좋음
#
# else 문은 예외가 발생하지않았을때만 실행되고
# finally 는 무조건 실행됨.

# raise 키워드로 예외 직접발생시키기

try:
    a = 'Park'
    if a == 'Kim':
        print('ok, pass')
    else:
        raise ValueError
        # 벨류에러는 이 조건에선 발생할수없는것이지만 직접설정가능
except VlaueError:
    print('Occurred, Exception')
else:
    print('ok! else')
