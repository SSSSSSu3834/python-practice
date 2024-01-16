#theater_module에 있는 모듈 불러오기

import theater_module
theater_module.price(3)  # 3명이서 영화보러 갔을 때 가격
theater_module.prince_morning(4) # 4명이서 조조할인 영화 보러 갔을 때
theater_module.price_soldier(5)  # 5명의 군인이 영화 보러 갔을 때


import theater_module as mv  
# theater_module의 이름을 mv로 정의해서 쓸 수 있다. 
mv.price(3)
mv.prince_morning(5)


from theater_module import *
# theater_module에 있는 모든 모듈을 가져오겠다는 뜻
# theater_module을 적어주지 않아도 됨
price(6)
prince_morning(5)



from theater_module import price, prince_morning
# 원하는 함수만 가져올 수 있다. 
price(1)
prince_morning(2)


from theater_module import price_soldier as price
# price_soldier만 가져와서 price라는 이름을 붙여 사용하겠다.
price(1)