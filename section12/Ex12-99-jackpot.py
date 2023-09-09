'''
파일명 : Ex12-99-jackpot.py
'''

import random
import time


pot = [n for n in range(1, 46)]

jackpot = []

for n in range(1, 7):   # 1 ~ 6
    random.shuffle(pot) # 리스트 순서 섞는다.

    pick = pot.pop()
    print(f'{n}번째 당첨번호는 {pick}입니다.')

    jackpot.append(pick)
    time.sleep(1)   # 1초 동안 프로그램 일시정지

jackpot.sort()
print(f'이번 당첨번호는 {jackpot} 입니다.')