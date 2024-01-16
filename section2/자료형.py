# 자료형
# 문자열도 곱하기가 된다
print("ㅋ"*9)

# 불리언 자료형
print(not True)
print(not False)
print(5<10)

# 변수
animal ="강아지"
name="연탄이"
age = 4
hobby = "산책"
is_adult = age>=3

print("우리집" + animal+"의 이름은"+ name+"이에요")
# 정수형을 + 와 함께 출력할 때는 str을 붙여서 문자형으로 만들어줘야한다.  
print(name+ "는"+ str(age)+"살이며," + hobby+"를 매우 좋아해요")
# 불리언을 출력할 때는 str을 붙여서 문자형으로 만들어줘야한다.  
print(name+"는 어른일까요?"+ str(is_adult))


#문자열을 연결할 때 + 말고 , 를 사용해도 된다. 
# 콤마를 사용하면 str을 붙이지 않아도 된다. 
#하지만 , 사이에 무조건 띄어쓰기가 들어간다.
print(name, "는", age,"살이며," , hobby,"를 매우 좋아해요")