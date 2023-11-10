# 결석한 친구들 제외하고 책 읽도록 시키기

#continueㄹㄹ 만나면 밑에 문장은 실행하지않고 다시 반복문으로 올라감
# break만나면 바로 함수 끝!
absent = [2,5] #결석
noBook = [7] # 책을 안가져옴

for student in range(1,11):
    if student in absent:
        continue
    elif student in noBook:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와" .format(student))
        break
    print("{0}, 책을 읽어봐" .format(student))

