# 파일 만들고 열어서 글쓰기
# (파일이름, "w") : w는 쓰기 목적
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0",file=score_file)
print("영어 : 50",file=score_file)
score_file.close()
# 파일 열었으면 항상 닫아줘야함
# vscode 내부에 score.txt 파일이 생김


# 이미 존재하는 파일에 이어서 쓰고 싶을 때 a를 써준다. 
# write를 쓸 때는 줄바꿈을 명시적으로 적어줘야한다.
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학: 80")
score_file.write("\n미술: 40")
score_file.close()

