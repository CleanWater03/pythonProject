'''
파일명 : Ex11-6-variable-local-global.py

지역변수(local)
    함수 내부에 선언
    함수 내부에서만 사용이 가능한 변수
    함수 종료 시 같이 소멸된다.

전역변수(global)
    함수 외부선언
    함수 내부 외부 모두 사용 가능하다.
    프로그램 종료 시 소멸된다.
'''

gVar = '전역'
def globalAndLocal():
    lVar = '지역'
    print(f'{gVar} 변수 입니다.')
    print(f'{lVar} 변수 입니다.')

def globalAndLocal2():
    lVar = '지역2'
    print(f'{gVar} 변수 입니다.')
    print(f'{lVar} 변수 입니다.')

globalAndLocal()
globalAndLocal2()