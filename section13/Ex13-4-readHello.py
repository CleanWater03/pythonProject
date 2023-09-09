'''
파일명 : Ex13-4-readHello.py

open() 함수 모드
    r(read mode) : 읽기 전용 모드 / 파일이 없으면 에러

경로(path)
    파일 시스템에서 파일이나 디렉토리 위치를 나타내는 문자열.

    1. 절대경로
        파일 시스템 루트 디렉토리부터 출발하여 파일이나 디렉토리를 찾는 경로.
        ex) C:\pstudy\pythonProject\section13\hello.txt
        Linux, Mac - /

    2. 상대경로
        현재 작업 디렉토리를 기준으로 파일이나 디렉토리를 찾는 경로
        ex) ./hello.txt
            . -> 현재 경로를 나타낸다.
            .. -> 상위 폴더를 나타낸다.
'''

'''
file = open('hello.txt', 'rt', encoding='UTF-8')
str = file.read()
print(str, end='')
file.close()
'''

# with문으로 변경
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    str = file.read()
    print(str, end='')