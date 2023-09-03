'''
파일명 : Ex11-3-function3.py
'''

# 반환(return) 값이 있는 함수
# 매개변수 x, 리턴 o -> 함수가 실행되고 결과 또는 값을 반환해준다.
def address():
    str = '''우편번호 12345
    서울시 영등포구 여의도동
    '''
    return str

result = address()
print(result)

# 함수 안에서 함수 호출 가능
print(address())

def plus(num1, num2)
    return num1 + num2

result = plus(5, 7)
print(result)
print(plus(2, 3))