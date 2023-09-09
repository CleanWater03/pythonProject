'''
파일명 : Ex13-8-readhello5.py
'''

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()  # readlines가 hello.txt를 list로 반환시켜준다.
    for no, line in enumerate(line_list):
        print(f'{no+1} {line}', end='')
