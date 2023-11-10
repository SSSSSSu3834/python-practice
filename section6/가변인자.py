# 인자의 개수가 바뀐다
#print문에서 줄바꿈 없애고 싶을 때 end=" " 적어주면 된다.
def profile(name, age,*language):
    print("이름:{0}\t 나이:{1}\t" .format(name, age), end = " ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("gustn", 20, "sdf", "python", "java")
profile("현진", 21, "python", "java")
# 이름:gustn       나이:20         sdf python java