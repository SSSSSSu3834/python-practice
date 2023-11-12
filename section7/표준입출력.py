# sep="":  콤마로 연결된 문자열의 결합 사이에 넣고 싶은 값을 넣어준다.
# end = "": 끝부분을 명시적으로 적어주면 다음에 나오는 출력문과 한줄로 출력된다.
print("python", "java", " javascript", sep=" vs ", end="?")
print("무엇이 더 재미있을까요?")

import sys
# stdout은 표준출력으로 문장이 찍히는 것
print("Python", "java", file=sys.stdout)
# stderr은 표준 에러로 출력되는 것(에러처리할 떄 사용)
print("Python", "java", file=sys.stderr)

# 시험 성적 정렬하기
# dictionary를 쓸 때는 itemes라는 메서드를 쓰면 key와 value값 을 튜플로 보내준다.
score = {"수학": 0, "영어": 50, "코딩":100}
for subject, score in score.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
# 과목명은 8칸을 만든다음에 left정렬
# 점수는 4칸을 만든다음에 right정렬


#은행 대기순번표
# 001 002 003 ...
for num in range(1,21):
    print("대기번호: " + str(num).zfill(3))
    # zfill(숫자) : 3개만큼의 공간을 확보하고 나머지는 0으로 채워달라


#표준입력 (사용자입력)
# 사용자 입력으로 받으면 타입은 항상 문자열이다. 
answer = input("아무값이나 입력하세요: ")
print("입력하신 값은 " + answer + "입니다")