# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
       
# 일반 유닛을 상속 받은 공격유닛
# 상속 받을 유닛은 괄호안에 넣어준다.
# 상속받은 클래스의 생성자를 써준다.
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" 
              .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다." .format(self.name))  

# 공격캐릭터 만들기
firebat1 =AttackUnit("파이어뱃", 50, 16)
# 공격하기
firebat1.attack("5시")
#공격당하기
firebat1.damaged(25)
firebat1.damaged(25)