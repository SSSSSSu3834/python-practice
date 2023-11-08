#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#  예)http://naver.com
# 규칙1: http:// 부분은 제외
# 규칙2: 저음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 개수+ 글자 내 'e' 개수 + "!" 로 구성
# 예) 생성된 비밀번호: nav51!

origin = "http://naver.com"
# origin = "http://daum.com"

# (http://) 를 잘라서 없애줌
id=origin[7:]

# .이 몇 번째에 들어가있는지 알려줌=> 5
dotIndex = id.index(".")

# 처음부터 점(.)이 찍혀있는 곳 전까지 잘라줌
site = id[:dotIndex]

password = site[:3] + str(len(site)) + str(site.count("e")) + "!" 

print("{}의 비밀번호는 {}입니다" .format(site,password))