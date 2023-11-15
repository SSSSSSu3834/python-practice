# 게임 만들기

# 일반 유닛
from hmac import new
from random import *


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{}이 생성되었습니다." .format(self.name))
    def move(self, location):
        print("지상유닛이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
               .format(self.name, location, self.speed))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다." .format(self.name))  

        
       
# 일반 유닛을 상속 받은 공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        # 상속받은 생성자 써줘야함
        Unit.__init__(self, name, hp,speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" 
              .format(self.name, location, self.damage))
    
  
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

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    # 스팀팩 : 일정시간동안 이동 및 공격속도 증가, 체력 10감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{} : 스팀팩을 사용합니다 (hp 10 감소)" .format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다." .format(self.name))


# 탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격가능. 이동 불가
    seize_developed = False # 시즈모드 개발여부


    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 현재 시즈모드가 아닐때 => 시즈모드 on
        if self.seize_mode == False:
            print("{} : 시즈모드로 전환합니다" .format(self.name))
            self.damage *=2
            self.seize_mode = True
        # 현재 시즈모드일 떄 => 시즈모드 off
        else: 
             print("{} : 시즈모드를 해제합니다" .format(self.name))
             self.damage /=2
             self.seize_mode = False


# 레이스 - 공중유닛
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스", 80, 20, 5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked ==True:
            print("{} : 클로킹 모드를 해제합니다" .format(self.name))
            self.clocked = False
        else:
            print("{} : 클로킹 모드를 설정합니다" .format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다 ")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")



# 실제 게임 진행
game_start()

# 마린 3개 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()


# 탱크 2개 생성
t1 = Tank()
t2 = Tank()

# 레이스 1개 생성
w1 = Wraith()


# 유닛 일괄 관리 (생성된 모든 유닛을 append해서 배열에 넣어줌)
attact_units = []
attact_units.append(m1)
attact_units.append(m2)
attact_units.append(m3)
attact_units.append(t1)
attact_units.append(t2)
attact_units.append(w1)

# 전군 이동
for unit in attact_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed =True
print("[알림] 탱크 시주모드 개발이 완료되어습니다.")


# 공격모드 준비(마린 : 스팀팩, 탱크: 시즈모드, 레이스 : 클로깅)
for unit in attact_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    if isinstance(unit, Tank):
        unit.set_seize_mode()
    if isinstance(unit, Wraith):
        unit.clocking()


# 전군 공격
for unit in attact_units:
    unit.attack("1시")

# 전군 피해 : 공격은 랜덤으로 받음
for unit in attact_units:
    unit.damaged(randint(5,21))

# 게임 종료
game_over()