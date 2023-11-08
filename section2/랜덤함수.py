#랜덤 라이브러리 사용
from random import *

# 0.0 ~ 1.0 미만의 아무 수나 뽑아줌
print(random())
# 0.0 ~ 10.0 미만의 아무 수나 뽑아줌
print(random()*10)
print(random()*10//1)  #실수
print(int(random()*10))  #정수

#1~10 이하의 랜덤수
print(int(random()*10)+1)

#로또값 출력(1~45)
print(int(random()*45 )+1)
print(randrange(1,46)) #1~46 미만의 값 생성
print(randint(1,45)) #randint는 양쪽값을 모두 포함함