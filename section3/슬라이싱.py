# 원하는 값만 잘라서 가져오고 싶을 때
jumin = "020101-1234567"

print("성별:"+ jumin[7])
print("년도:"+ jumin[0:2]) # 0부터 2전까지
print("월:"+ jumin[2:4])
print("일:"+ jumin[4:6])

print("생년월일:"+ jumin[0:6])
#둘 다 똑같은 뜻 : 처음부터 6전까지
print("생년월일:"+ jumin[:6])


#주민등록 뒤 7자리 가져오기
print("뒤 7자리: " + jumin[7:])   
#맨 뒤(-1)에서 7번째(-7)부터 끝까지
print("뒤 7자리(뒤에서부터): " + jumin[-7:])