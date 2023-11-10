#while 문은 조건에 맞을 떄까지 계속 함수를 반복한다. 

customer = "현수"
index = 5
while (index >= 1):
    print("{0}님 커피가 준비되었습니다. {1}번 남았어요." .format(customer, index))
    index-=1
    if index ==0:
        print("커피는 폐기처분 되었습니다")


# 해당하는 손님이 왔는지 검사하기
customer2 = "토르"
person = "Unknown"

while person !=customer2:
    print("{0}님 커피가 준비되었습니다" .format(customer2))
    person = input("이름이 어떻게 되세요? : ")
    if person == customer2 :
        print("{0}님 커피 맛있게 드세요" .format(customer2))