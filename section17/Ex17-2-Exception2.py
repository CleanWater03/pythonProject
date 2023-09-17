'''
파일명: Ex17-2-Exception2.py

예외(Exception)
    프로그램 실행중 발생할 수 있는 오류나 예기치 않은 상황


예외처리방법
try:
    정상코드 영역
except:
    예외 발생시 처리 영역

'''

try:
    a = int(input('제수를 입력하세요 >>> '))
    b = int(input('피제수를 입력하세요 >>> '))
    print(f'{a} / {b} = {a / b}')
except:
    print('예외가 발생했습니다.')