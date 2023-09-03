'''
파일명 : Ex11-5-function5.py

다중 반환
    파이썬은 여러개의 반환값도 처리할 수 있다.
'''
def calculator(*args):
    return sum(args), sum(args)/len(args), max(args)

a, b, c, d = calculator(1, 2, 3, 4, 5)
print(f'합계: {a}')
print(f'평균: {b}')
print(f'최댓값: {c}')
print(f'최솟값: {d}')