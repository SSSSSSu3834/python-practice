# 집합 (set)
# 중복 안 됨, 순서 없음
# sort도 해줌
my_set = {1,2,2,23,3,4,4,4,4,}
print(my_set)


# 교집합: 두 언어 둘 다 할 수 있는 개발자를 찾자
java = {"현수", "현진" , "경라"}
python = set(["현수", "유담"])  # 이것도 set 정의하는 방법

print(java & python)  # {'현수'}
print(java.intersection(python))   # {'현수'}

# 합집합 찾기: 자바 또는 파이썬을 할 수 있는 사람
print(java | python)
print(java.union(python))  # {'경라', '유담', '현수', '현진'}


# 차집합 찾기 ( 자바 - 파이썬)
print(java - python)
print(java.difference(python))  # {'경라', '현진'}


# 파이썬을 할 줄 아는 사람이 늘어났을 떄
python.add("승우")
print(python)  # {'승우', '유담', '현수'}


# java를 더이상 할 수 없게 됐을 떄 
java.remove("현진")
print(java)    # {'경라', '현수'}