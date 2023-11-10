subway = ["유재석", "조세호", "박명수"]

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))  #1

#다음 정류장에서 하하가 탔다.
subway.append("하하")
print(subway)

# 정형돈을 유재석/조세호 사이에 태워봄(원하는 순서, "넣고 싶은 것")
subway.insert(1, "정형돈")
print(subway)  # ['유재석', '정형돈', '조세호', '박명수', '하하']


#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # 하하
print(subway)  # ['유재석', '정형돈', '조세호', '박명수']

# 같은 이름의 사람이 몇 명 있는지 확인하기
subway.append("유재석")
print(subway.count("유재석"))  #2


# 정렬
num_list = [5,4,2,3,1]
num_list.sort()
print(num_list)


#정렬순서 뒤집기
num_list.reverse()
print(num_list)

# 배열 모두 삭제하기
# num_list.clear()
# print(num_list)


# 다양한 자료형 함께 사용 가능!
mix_list = ["dk", 23, True]

# 리스트 합치기
num_list.extend(mix_list)
print(num_list)