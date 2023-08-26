'''
파일명 : Ex02-3-type.py

내장 데이터 유형
    Python 변수는 다른 유형의 데이터를 저장할 수 있으며
    다른 유형은 다른 작업을 수행할 수 있다.

텍스트 유형(문자열) : str - string이라고 읽음.
숫자 유향 : int(정수형), float(실수형)
시퀀스 유형 : list, tuple, range
매핑 유형 : dict - dictionary라고 읽음.
세트 유형 : set
논리 유형 : bool
바이너리 유형 : bytes
없음 유형 : None
'''
x = 'Hello, World'
print(type(x))

# int - 정수형(integer)을 의미함.
x = 20
print(type(x))

# float - 실수형을 의미함.
x = 20.5
print(type(x))

# list - 한 변수에 여러 값을 넣을 수 있음.
x = ['피카츄', '라이츄', '파이리']
print(type(x))

# tuple - 한 번 값이 들어가면 변경이 안된다!
x = ('피카츄', '라이츄', '파이리')
print(type(x))

# range - 여러 값을 범위로써 지정.(0부터 지정)
x = range(6)
print(type(x))

# dict - 사전 형태의 변수를 지정.
x = {'name':'피카츄', 'skill': '백만볼트'}
print(type(x))

# set - 일련의 집합을 중괄호를 통해 나타냄. 중복값이 들어가지 않는 타입임.
x = {'피카츄', '라이츄', '파이리'}
print(type(x))

# bool(논리)
x = True # False
print(type(x))

# NoneType - 아무 값도 없음을 나타냄.
x = None
print(type(x))

#입력하는 값에 따라 변수의 형태가 달라짐

'''
변수명 = 값
값이 type에 따라 연산이 달라진다.
예) 더하기 경우
    숫자 + 숫자 = 숫자
    문자 + 문자 = 문자연결
    문자 + str(숫자) = 문자숫자연결
'''
num1 = 10
num2 = 20
result = num1 + num2
print(result)

name = 'Alice'
age = '15'
result = name + '/' + age
print(result)
# 문자끼리의 더하기는 연산이 아니라 연결이 된다.

name = '피카츄'
age = 28
result = name + str(age)    #문자 + str(숫자) 형변환필요
print(result)