gun = 20

# def chechpoint(soldiers):
#     gun = gun-soldiers
#     print("[함수 내] 남은 총: {}".format(gun))

# 함수안에서 gun은 지역변수이므로 만들지 않으면 쓸 수 없다. 
# 만약 전역변수 gun을 사용하고 싶다면 global gun 으로 선언한다. 

def chechpoint(soldiers):
    global gun # 전역변수 gun 사용
    gun = gun-soldiers
    print("[함수 내] 남은 총: {}".format(gun))

chechpoint(2)


# 전역변수를 많이 사용하는 건 좋지않다.
# 전역 변수를 인자에 넣고 return 값으로 전역변수 값을 다시 정의하자
def checkpoint_ret(gun, soldiers):
    gun = gun- soldiers 
    print("[함수 내] 남은 총: {}".format(gun))
    return gun

gun  = checkpoint_ret(gun, 15)
print(gun)