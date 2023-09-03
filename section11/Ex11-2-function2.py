'''
파일명 : Ex11-2-function2.py
'''

# 매개변수 o, 리턴 x -> 매개변수 입력값을 받아 실행하는 함수
def introduce(name, age):   # name = '홍길동', age = 25
    print(f'내 이름은 {name}이고, 나이는 {age}살입니다.')

introduce('홍길동', 25)

# 가변 매개변수 함수
def show(*args):
    print(type(args))
    for item in args:
        print(item)

show('Python')
show('Python', 'Java', 'C++', 'Ruby', 'Go')