'''
파일명 : Ex13-7-readhello4

realines() - 줄 단위 요소로 리스트 타입으로 변환
'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()    # readlines가 hello.txt를 list로 반환시켜준다.
    for line in line_list:
        print(line, end='')
