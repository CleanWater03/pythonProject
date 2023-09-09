'''
파일명 : Ex13-2-makeHello.py

open() 함수 모드
    w(write mode) : 쓰기 전용모드 / 파일이 없으면 생성
    t(text mode) : 해당파일의 데이터를 텍스트 파일로 인식하고 입출력
'''
# 인코딩 코드를 설정해야 파이썬 내부에서 정상적으로 파일이 생성된다.
file = open('hello.txt', 'wt', encoding='UTF-8')
file.write('안녕하세요.')
file.write('\n')
file.write('반갑습니다.')
file.write('\n')
print('hello.txt 파일이 생성되었습니다.')
file.close()
