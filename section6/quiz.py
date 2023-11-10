# Qu12) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 제중 : 각 개인의 키에 적당한 제중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 제중은 별도의 함수 내에서 계산
#         * 함수명 : std_welght
#         * 전달값 : 키(height), 성별 (gender)
# 조건2 : 표준. 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
   if gender =="여자":
       std = ((height/100)**2)*21
       print("키 {0}cm {1}의 표준체중은 {2}kg 입니다." .format(height, gender, round(std ,2)))
   elif gender =="남자":
        std = ((height/100)**2)*22
        print("키 {0}cm {1}의 표준체중은 {2}kg 입니다." .format(height, gender, round(std, 2)))


std_weight(180, "남자")