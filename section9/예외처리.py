try:
    print("나누기 전용 계산기입니다.")

    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))

    print("{0} / {1} = {2}" .format(num1, num2, num1/num2))
except ValueError:
    print("잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print(err)   # division by zero
except Exception as err:
    print("알 수 없는 에러가 발생했습니다") # 어디에도 해당하지 않는 에러를 잡아냄
    print(err) # 정확한 에러메시지 보여줌(ex.배열에 없는 값이다)

    
