'''
파일명 : Ex16-5-inheritance.py

상속(inheritance)
    상위클래스(부모클래스, 슈퍼클래스)가 가지고 있는 기능을
    그대로 물려받아 하위클래스(자식클래스, 서브클래스)에서
    사용할 수 있다.

상속방법
class 상위클래스:
    본문
'''
# 상위클래스(부모클래스)
class coffee:
    def __init__(self,bean):
        self.bean = bean

    def coffe_info(self):
        print('원두: {}'.format(self.bean))

# 하위클래스(자식클래스)
class Espresso(coffee):
    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print(f'물:{self.water}ml')

# 실행코드
coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()

print(coffee.bean)
coffee.coffe_info()