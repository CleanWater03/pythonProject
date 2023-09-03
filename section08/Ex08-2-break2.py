'''
파일명 : Ex08-2-break2.py
'''
while True:
    city = input('대한민국의 수도는 어디인가요? >>> ')
    if city == '서울' or city == 'seoul' or city == 'SEOUL':
        print('정답입니다.')
        break
    else:
        print('오답입니다. 다시 시도하세요.')