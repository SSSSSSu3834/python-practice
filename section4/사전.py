#사전형 => 객체랑 비슷한 개념
cabinet = {3: "유재석", 100: "김태호"}
# 값 가져오기
print(cabinet[3]) # 유재석
print(cabinet.get(3)) # 유재석

# 만약 없는 key 값을 가져오라고 했을 때 []를 사용하면 프로그램이 종료되고 
# get을 사용하면 Nene이라고 뜨고 계속 프로그램을 진행한다. 

# 자료형이 존재하는지 확인
print(3 in cabinet) # true
print (5 in cabinet) # false

# 객체에 항목 추가하고 싶을때
cabinet[5] = "조세호"
print(cabinet)
# 만약 같은 key를 가지도록 값을 설정한다면 덮여씌워진다. 
cabinet[3] = "뽀로로"
print(cabinet)

# key 값 삭제하기
del cabinet[3]
print(cabinet)


# key값만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())


# key와 value 모두 출력
print(cabinet.items())


# 모든 값 삭제
print(cabinet.clear()) # None