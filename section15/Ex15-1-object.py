'''
파일명 : Ex15-1-object.py

클래스(class)
    클래스는 객체를 생성하기 위한 템플릿.
    객체를 만드는 설계도
    붕어빵 틀, 와플 기계
    객체화(인스턴스화) - 메모리에 올리는것

객체(object)
    현실 세계 존재하는 물리적인 것 또는 추상적인 개념을
    프로그램으로 표현한 것. (식별 가능한 것)
    예) 물리적 객체 - 컴퓨터, 자동차, 마우스, 모니터, 키보드 등.
        추상적 객체 - 주문, 영수증, 게임유닛


객체 구성
    속성 - 변수
    기능 - 메소드(method)
'''

class Computuer:
    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print(f'CPU = {self.cpu}')
        print(f'RAM = {self.ram}')
        print(f'VGA = {self.vga}')
        print(f'SSD = {self.ssd}')

# 실행 코드
desktop = Computuer()   # Computer 객체 생성
desktop.set_spec('i7', '32GB', 'RTX4070TI', '2TB')