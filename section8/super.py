# super
# super()를 쓸 때는 self를 적어주지 않는다


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


# 상속받은 애들의 생성자를 써줄 땐 super()을 써서 해줘도 된다.
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
     # Unit.__init__(self, name, hp, 0)
     super().__init__(name, hp, 0)
     self.location = location



# 서플라이디폿
supply_depot = BuildingUnit("서플라이디폿", 500, "7시")

