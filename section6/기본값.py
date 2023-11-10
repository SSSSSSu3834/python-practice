def profile(name, age, main_leng):
    print("이름: {0} \n나이: {1} \n사용언어: {2}"   
        .format(name, age, main_leng))   
    
profile("현수", 20, "js")

# 기본값 사용하여 입력하지 않아도 값이 채워지도록 만들 수 있다.
# ex) 같은 학년이어서 나이가 고정값일떄

def profile2(name, age=17, main_leng="js"):
    print("이름: {0} \t나이: {1} \t사용언어: {2}"   
        .format(name, age, main_leng))   
    
profile2("현수")
profile2("현진")
profile2("경라")