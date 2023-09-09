'''
파일명 : Ex13-6-readHello.py

readline() 함수
    파일에서 1줄을 일고 그 결과를 반환 한다.
'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    while True:
        str = file.readline
        if not str: # 읽을 값이 없으면 Ture가 된다.
            break
        print(str, end='')