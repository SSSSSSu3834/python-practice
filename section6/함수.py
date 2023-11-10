# def 함수이름():
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 입금하는 함수
def deposit(잔액, 입금금액):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다." .format(잔액+입금금액))
    return 잔액+입금금액

# 출금하는 함수
def withdraw(잔액, 출금금액):
    if 잔액 < 출금금액:
        print("{0}보다 적은 금액을 입력하세요" .format(잔액))
        return 잔액
    print("출금이 완료되었습니다. 잔액은 {0}원입니다." .format(잔액-출금금액))
    return 잔액-출금금액


# 저녁 출금으로인한 수수료
def withdraw_night(잔액, 출금금액):
    commission = 100 #수수료 100원
    return commission, 잔액 - 출금금액- commission  #튜플형식으로 여래가 값 반환

잔액 = 0
잔액 = deposit(잔액, 1500)
print(잔액)
잔액 = withdraw(잔액, 1000)
print(잔액)

commission, 잔액 = withdraw_night(잔액, 200)
print("수수료는 {0}원이며, 잔액은 {1}원입니다." .format(commission, 잔액))