# 한 줄로 끝내는 for 문

# 출석번호 1 2 3 4 앞에 100을 붙이기로 함 => 101 102 ...

students = [1,2,3,4,5]
# students에 있는 i 값을 하나씩 불러와서 100을 더해주겠다는 뜻
students = [i+100 for i in students]
print(students)

#학생 이름을 길이로 변환
students = ["sdfs", "sdfsdfsdf", "ddd1d"]
students = [len(i) for i in students]
print(students)


# 학생 이름을 대문자로 변환
students = ["sdfs", "sdfsdfsdf", "ddd1d"]
students = [i.upper() for i in students]
print(students)