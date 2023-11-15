# pass
# 아무것도 안 하고 일단 넘어간다. 
# 아무것도 쓰지 않아도 프로그램이 종료되지 않는다


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


# 건물이 일단은 완성된 것처럼 보임
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# 서플라이디폿
supply_depot = BuildingUnit("서플라이디폿", 500, "7시")
# 아무것도 안 찍힘
