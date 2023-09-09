'''
파일명 : Ex12-2-module2.py

모듈 사용법
함수 1개 사용 : from 모듈명 import 함수
함수 여러개 사용 : from 모듈명 import 함수1, 함수2
함수 전체 사용 : from 모듈명 import *
'''

from converter import kilometer_to_miles

miles = kilometer_to_miles(150)
print(f'150km = {miles}miles')