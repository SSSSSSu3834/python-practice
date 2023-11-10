# 매개변수 키워드를 사용해서 인자로 넣어주면 순서에 상관없이 
# 키워드에 따라 잘 매치가 된다.

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name ="ggustn", main_lang= "파이썬", age = 20)