# 텍스트 상태의 데이터가 아닌 파이썬 객체 자체를 파일로 저장하는 것 입니다.

import pickle
# pickle은 'wb" b라는 바이너리 형태를 꼭 붙여줘야한다.
profile_file = open("profile.pickle", "wb")

profile = {"이름": "김현수" , "나이":22, "취미": ["축구", "야구", "농구"]}
print(profile)
# profile에 있는 정보를 file에 저장
pickle.dump(profile, profile_file)
profile_file.close()


# 파일에 있는 값 불러오기
profile_file = open("profile.pickle", "rb")
# file에 있는 정보를 profile 변수에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()