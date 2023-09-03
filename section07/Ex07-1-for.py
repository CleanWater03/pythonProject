'''
파일명 : Ex07-1-for.py

for문
    값의 범위나 횟수가 정해져 있을 때
    사용하면 편리한 반복문
    while문 보다 사용 빈도가 높다.

for 변수 in 반복 가능한 객체 :
    반복실행문
'''

for n in [1, 2, 3]:
    print(n)    # print(1), print(2), print(3)

'''
string을 사용하지 않는 for문
for ch in 'abcde':
    print(ch)
'''
# string을 사용하는 for문
str = 'abcde'
for ch in str:
    print(ch)
