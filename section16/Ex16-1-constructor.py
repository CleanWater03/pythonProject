'''
파일명 : Ex16-1-constructor.py

생성자
    객체를 생성할 때 자동으로 실행(호출)되는 메소드
    주로 객체 초기화 용으로 사용된다.

생성자 선언 방법
    __init()__
'''

class USB:
    def __init__(self, capacity):
        self.capacity = capacity

    def info(self):
        print(f'{self.capacity}GB USB')

# 실행 코드
usb = USB(128)
usb.info()

usb2 = USB(1024)
usb2.info()