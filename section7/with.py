# with를 사용하면 파일을 닫아줄 필요없다.

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


with open("study.txt", "w" ,encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하는 중")


with open("study.txt", "r" ,encoding="utf8") as study_file:
    print(study_file.read())