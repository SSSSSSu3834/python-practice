# 파일 출력: read 의 r을 써준다. 
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())

# 파일의 내용을 한 줄 한 줄 불러오고 싶을 때
# 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()
# 수학 : 0
# 영어 : 50
# 과학: 80
# 미술: 40


# 만약에 파일내에 몇 줄 있는지 모를때
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()


# 리스트에 넣어서 처리하기
# readlines 메서드를 사용하면 모든 라인을 가져와서 리스트에 저장함
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()