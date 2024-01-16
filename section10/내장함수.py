# input
# dir : 어떤 객체를 넘겨줬을 때 그객체가 어떤 변수와 함수를 가지고 있는지 알려줌
# print(dir())
# import random
# print(dir())  # random함수 추가됨
# import pickle
# print(dir())

# 모듈에서 어떤 함수를 쓸 수 있는지도 알려줌
# print(dir(random))

# 리스트에서 쓸 수 있는 내용들 나옴
list = [1,2,3]
print(dir(list)) 


# 문자열
name = "Jim"
print(dir(name))