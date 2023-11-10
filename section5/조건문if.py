
# 날씨에 대한 해당 단어가 포함되면 조건문에 따라 문장이 나오도록 함
weather = input("오늘 날씨는 어때요? : ")

# 입력된 문장에 비나 눈이 포함되어 있으면 우산을 챙기세요 출력
if weather.find("비" or "눈") != -1:
    print("우산을 챙기세요")
elif weather.find("미세먼지") != -1:
    print("마스크를 챙기세요")
else: 
    print("준비물 필요 없어요!")



temp = int(input("기온은 어때요?: "))
# 사용자가 입력한 값을 int형으로 바꿔준다.

if 30 <= temp:
    print("너무 더워요. 외출을 자제하세요") 
elif 10 <= temp and temp <30:
    print("괜찮은 날씨네요!")
elif 0<= temp <10:
    print("외투를 챙기세요")

else:
    print("너무 추워요! 나가지 마세요!")

