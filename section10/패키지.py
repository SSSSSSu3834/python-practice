import travel.thailand  # 모듈이나 패키지만 import 할 수 있다. 
# import travel.thailand.ThailandPackage => X 
# 하지만 from ~ import 구문에서는 함수나 클래스도 가져올 수 있다.
# from travel.thailand import ThailandPackage

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to2 = vietnam.VietnamPackage()
# trip_to2.detail()


from travel import *
# trip_to2 = thailand.ThailandPackage()
# trip_to2.detail()


# 모듈 위치를 알아보자
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

# C:\Python311\Lib\random.py
# d:\파이썬\파이썬 실습\.vscode\python-practice\section10\travel\thailand.py