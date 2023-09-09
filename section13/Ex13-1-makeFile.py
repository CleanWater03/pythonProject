'''
파일명 : Ex13-1-makeFile.py

파일 입출력(I/0 - Input/Output)
    입력(Input) 기존 파일 읽어들이는 것.
    출력(Output) 파일 생성, 내용 추가를 말한다.

open() 함수
    파이썬에서 open() 함수를 사용하여 파일을 열고 파일객체 생성,
    이를 통해 파일을 일고 쓸 수 있다.
'''

# open 함수를 사용하면 괄호 안의 이름으로 파일이 새로 생성되게 된다.
'''
file = open('myFile.txt','wt')
print('myFile.txt 파일이 생성되었습니다.')
file.close()
'''

# with 문 - 자동으로 close()를 해준다.
with open('myFile.txt', 'wt') as file:
    file.write('with')
    print('myFile.txt 파일이 생성되었습니다.')

