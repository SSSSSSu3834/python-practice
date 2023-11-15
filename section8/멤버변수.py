# 멤버변수는 필드같은 거 
# 정적인 변수라고 생각하면 됨
# class 바깥에서 객체안에 내장되어있는 변수로서 사용할 수 있음

#self.name = name
# self.hp = hp
# self.damage = damage

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성 되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

wraith1 = Unit("레이스" ,80 ,5)
print("유닛이름: {0}, 공격력: {1}" .format(wraith1.name, wraith1.damage))

# 레이스 기능 추가
wraith2 = Unit("레이스", 80,5)
wraith2.clocking = True

if wraith2.clocking ==True:
    print("{}는 현재 클로깅 상태입니다." .format(wraith2.clocking))