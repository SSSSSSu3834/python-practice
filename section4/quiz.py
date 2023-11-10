# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)

#  --당첨자 발표--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#  --축하합니다--


#(활용 예제)
#from random import *
#lst = [1,2,3,4,5]
#print(lst)
#shuffle(lst)  # 배열을 무작위로 섞어줌
#print(lst)
#print(sample(lst, 1))  # 리스트에서 1명 뽑아줌


#====1명 뽑고 리스트에서 지우고 3명 뽑기==================
from random import *
id = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
shuffle(id)
chicken = sample(id, 1)
print(chicken)

# id를 set으로 바꿔서 remove쓸 수 있도록 함
id = set(id)
# id 집합에서 chicken으로 뽑았던 수 없애줌
id.remove(chicken[0])
print(id)

# id에서 커피 줄 애 뽑음(sample은 list에서 사용할 수 있으니 자료구조 변경)
coffee = sample(list(id),3)
print(coffee)

print("--당첨자 발표!!!--")

print("치킨 당첨자: " + str(chicken[0]) )
print("커피 당첨자: " + str(coffee))

print("--축하합니다!!!--")



# =================4명 뽑고 (1 / 3)으로 분배하기 =====================
id2 = range(1,21) # 1 ~ 20 까지 수 생성 (type은 range라서 배열로 바꿔야함)
id2 = list(id2)

shuffle(id2)
pick = sample(id2, 4)
print(pick)
print("--당첨자 발표!!!--")

print("치킨 당첨자: " + str(pick[0]) )
print("커피 당첨자: " + str(pick[1:]))

print("--축하합니다!!!--")

