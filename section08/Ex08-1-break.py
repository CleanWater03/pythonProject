'''
파일명 : Ex08-1-break.py

break문
    while문이나 for문과 같은 반복문을
    강제로 종료하는 명령어
'''
n = 1
while True:
    print(n)
    if n == 10:
        break
    n += 1

print('while end')