'''
파일명: Ex12-9-datetime.py

datetime
    날짜와 시간 데이터를 처리하는 모듈
    time보단 상세하게 시간 연산 가능
'''

import datetime
# 현재 날짜와 시간 반환, 마이크로초 단위 출력
print(datetime.datetime.now())
print(datetime.datetime.today())

# date() 함수 특정날짜를 만들어 반환
print(datetime.date(2023, 8, 15))
print(datetime.time(10, 40, 0))

# 날짜 필드값
y = datetime.datetime.now().year
m = datetime.datetime.now().month
d = datetime.datetime.now().day
h = datetime.datetime.now().hour
mi = datetime.datetime.now().minute
s = datetime.datetime.now().second

print(f'{y}년 {m}월 {d}일 {h}:{mi}:{s}')

# timedelta() 날짜/시간 데이터 연산
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)

date1 = datetime.date(2023, 9, 10)
date2 = datetime.date(2023, 12, 25)
print(date2 - date1)
print((date2 - date1).total_seconds())