'''
파일명 : Ex07-2-for2.py
'''

pwd = input('비밀번호를 입력하세요 >>>')

ch_count = 0
num_count = 0
for ch in pwd:
    if ch.isalpha():    # 문자 여부
        ch_count += 1
    elif ch.isnumeric():    # 숫자 여부
        num_count += 1

if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호입니다.')
else:
    print('불가능한 비밀번호입니다.')