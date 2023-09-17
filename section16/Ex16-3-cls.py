'''
파일명 : Ex16-3-cls.py

클래스 변수
    클래스를 기반으로 만든 모든 안스턴스(객체)가 공유할 수 있는 변수

인스턴스 변수
    해당 인스턴스(객체)만 사용하는 변수

클래스 메소드
    인스턴스가 없어도 클래스를 이용해 클래스 메소드 안에서 클래스 변수 접근 가능하다.
'''

class Bag:
    count = 0   # 클래스 변수(다른 언어에서는 스태틱 변수라고 말한다.)

    def __init__(self):
        Bag.count += 1

    @classmethod    # 데코레이터
    def sell(cls):
        cls.count -= 1

    @classmethod
    def remain_bag(cls):
        return cls.count

    @staticmethod


'''
클래스타입 / Bag() 형태로 테이블이 생성된다.
정적 영역 / bag 형식으로 추가.
'''
# 실행 코드
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print(f'현재 가방 : {Bag.remain_bag()}개')

bag2.sell()
print(f'현재 가방 : {Bag.remain_bag()}개')

bag3.sell()
print(f'현재 가방 : {Bag.remain_bag()}개')

Bag.slogan()