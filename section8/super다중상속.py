# super를 사용할 때 다중상속에 있어서 문제가 발생한다.
# 다중상속시 super를 사용하면 상속받는 순서에 따라서 상속이 이루어진다.
# (뒤에 있는 건 상속 안 됨)
# 따라서 다중상속시에는 부모클래스의 이름을 사용해서 나타내야한다.

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# super로 상속 받았을 때
dropship = FlyableUnit()  # flyable 생성자