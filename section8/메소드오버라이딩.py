# 메소드 오버라이딩
# 상속 받는 class에서 메소드를 재정의 하는 것이다. 
# 그러면 자식 class에서는 새로정의한 메서드가 호출된다.
# 기본적인 메소드를 부모 class에서 정의하고
# 자식 class에서 특징에맞게 재정의해서 쓰면 된다. 

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("지상유닛이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
               .format(self.name, location, self.speed))
        
       
# 일반 유닛을 상속 받은 공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        # 상속받은 생성자 써줘야함
        Unit.__init__(self, name, hp,speed)
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

# 날 수 있는 기능을 가진 클래스
class Flyable: 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" 
              .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스 - 다중 상속 받음
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        # 상속받은 생성자 써줘야함
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 스피디는 0
        Flyable.__init__(self, flying_speed)
    def move(self, location):
         print("공중유닛이동")
         self.fly(self.name, location)

# 벌쳐 : 지상유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10 ,20)

# 배틀크루저 : 공중유닛
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25,3)

# 지상인지 공중인지에 따라 다른 메서드 사용하기 귀찮음
vulture.move("11시")
battlecruiser.fly(battlecruiser.name,"9시")
# location만 넣어주면 됨
battlecruiser.move("10시")
