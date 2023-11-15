# 클래스 만들기
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성 되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

# 공격유닛
# 클래스 내부에서 메소드 앞에는 self를 무조건 적어준다
# 뜻은 this와 비슷하다. 멤버변수와 매개변수를 구별하기 위함.
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
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