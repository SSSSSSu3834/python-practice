# __init_ : 생성자 함수
# 객체가 만들어질때 자동으로 생성되는 부분
# 생성자에서 정의된 매개변수 개수만큼 인자로 받아줘야한다
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성 되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)