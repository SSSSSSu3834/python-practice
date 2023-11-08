python = "Python is Amazing"
# 모두 소문자로 바꾸기
print(python.lower())
# 모두 대문자로 바꾸기
print(python.upper())

#대소문자 확인하기
print(python[0].isupper())  #true

#문자열 길이 반환
print(len(python))

# 원하는 문자 찾아서 다른 글자로 바꾸기
print(python.replace("Python", "Java"))  # Java is Amazing

#문자가 어디에 있는지 찾기
index = python.index("n")  #5
print(index)

# 첫번째 인덱스 찾고 그 다음 인덱스를 찾을 수 있다. 
index = python.index("n", index+1)
print(index)   #15
print(python.find("n"))



#만약 문자열에 해당 글자가 없다면
print(python.find("Java")) # -1
print(python.index("Java")) # 오류(여기서 프로그램 끝남)


# 문자열에서 n이 총 몇 번 나왔는지
print(python.count("n"))