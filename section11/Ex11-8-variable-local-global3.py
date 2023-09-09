'''
파일명 : Ex11-8-variable-local-global3.py
'''
# 전역변수 선언
total = 0

def gift(dic, who, money):
    global total
    total += money
    dic[who] = money
'''
dic : 주소값, who : 문자열, money : 숫자
who의 값은 바꿔도 출력에서 달라지는 것이 없다.
다만, wedding값은 달라지게 된다.
'''

wedding = {}
name = '영희'
gift(wedding, name, 5)
gift(wedding, '철수', 6)
gift(wedding, '이모', 10)
print(f'축의금 명단: {wedding}')
print(f'전체 축의금: {total}')

# 데이터 영역과 힙과 스택으로 구분된다.