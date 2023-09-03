'''
파일명 : Ex09-2-builtin-function.py
'''

# abs() 절대값
result = abs(-10)
print(result)

# format() 문자 포맷 관련 함수
result = format(100000) # str(100000) 같다
result = format(100000, ',')    # 천단위 표시
print(result)

# max() 최대값 반환
result = max(1, 10)
print(result)
li = [5, 4, 7, 3, 2, 9]
result = max(li)
print(result)

# min() 최소값 반환
result = min(li)
print(result)

# pow() 거듭제곱 함수
result = pow(10, 2)
print(result)

# sorted() 함수 - 정렬
my_li = [5, 6, 3, 4, 1, 2]
result = sorted(my_li)
print(result)

# 역정렬
result = sorted(my_li, reverse=True)
print(result)

# zip() 함수 - 같은 인덱스 번호끼리 튜플로 묶어 줍니다.
names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for student in zip(names, scores):
    print(student)

for name, score in zip(names, scores):
    print(f'{name}의 점수는 {score}점입니다.')