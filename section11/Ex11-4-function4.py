'''
파일명 : Ex11-4-function4.py

함수의 종료를 위한 return
'''

def charge(energy):
    if energy < 0:
        print('0보다 작은 에너지는 충전 할 수 없습니다.')
        return  # charge() 함수의 종료를 의미한다.

    print('에너지가 충전되었습니다.')


# charge(1)
charge(-1)