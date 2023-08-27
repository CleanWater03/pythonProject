'''
파일명 : Ex03-2-print.py

print() 함수 사용법
    sep : 출력할 value의 구분 문자
    end : value 출력 후 출력할 문자 (기본값 '\n')
    file : 출력 방향 지정
'''
print('재미있는', '파이썬')
print('Python', 'Java', 'C', sep = ',')   # sep 옵션값 지정.

print('안녕', end = '') # end 옵션값 지정.
print('하세요')

fos = open('sample.py', mode = 'wt')
# open 함수를 사용하여 파일을 만들거나 파일을 읽어 올 수 있음.
# 파일에 대한 정보를 가져옴.
# wt는 byte mode.

print('print("Hello, World")', file = fos)
# file 함수를 통해 saample.py로 위치를 지정함.
# csv 파일도 이 함수를 통해 여는 것이 가능하다.
fos.close()
# 문서를 자동으로 열고 닫고 하는 것도 가능하다.