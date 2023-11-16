# finally: 예외처리 되든 안 되든 무조건 실행되는 구문

class BigNumberError(Exception):
    def __init__(self, msg):
       self.msg = msg
    def __str__(self):  # 예외 객체를 문자열로 출력할 때 유용
       return self.msg


# 한자리 숫자 계산기
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")

    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))

    if num1 >= 10 or num2 >= 10:
     # 에러 던지기
     raise BigNumberError("입fur값: {0}, {1}" .format(num1,num2))
    print("{0} / {1} = {2}" .format(num1, num2, num1/num2))
    
except ValueError:
   print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except BigNumberError as err:
   print("에러가 발생하였습니다")
   print(err)

finally:
   print("계산기를 이용해주셔서 감사합니다")