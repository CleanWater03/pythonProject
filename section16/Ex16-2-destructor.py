'''
파일명 : Ex16-2-destructor.py

소멸자
    인스턴스가 소멸될 때 자동으로 호출된다.

소멸자 선언방법
    __del()__
'''
class Service:
    def __init__(self, service):
        self.service = service
        print(f'{self.service} Service가 시작되었습니다.')

    def __del__(self):  # 소멸자
        print(f'{self.service} Service가 종료되었습니다.')

# 실행 코드
s = Service('길 안내')
del s

s = Service('커피 주문')

print('프로그램 종료!')