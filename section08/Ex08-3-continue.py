'''
파일명 : Ex08-3-continue.py

continue
    while 문이나 for 문과 같은 반복문을 강제로 건너뛰게 한다.
'''
total = 0
# range(1, 101) 1~100 까지 연속 된 수
for a in range(1, 101):
    if a % 3 == 0:  # 3의 배수
        continue
    total += a
    print(f'a: {a}, total {total}')

print(total)
