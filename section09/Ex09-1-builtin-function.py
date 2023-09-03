'''
파일명 : Ex09-1-builtin-function.py

내장함수
    파이썬에서 제공해주는 별도의 import 없이
    어디서든 사용할 수 있는 함수
'''
'''
chr() 함수
    아스키 코드를 문자로 반환하는 함수
'''
ch1 = chr(65)
print(ch1)

'''
eval() 함수
    매개변수로 받은 expression(=식)을
    문자열로 받아서 실행하는 함수
'''
expr = input('계산식을 입력하세요 >>> ')
result = eval(expr)
print(f'{expr}={result}')

# len() 데이터 길이
text = 'Hello, World!'
print(len(text))