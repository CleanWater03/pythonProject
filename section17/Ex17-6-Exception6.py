'''
Ex17-6-Exception6.py
'''

import traceback

try:
    score = int(input('점수를 입력하세요 >>> '))
    if score < 0 or score > 100:
        raise Exception('점수는 0~100 사이 입니다.')
except Exception as e:
    print(e)
    traceback.print_exc()
else:
    if score >= 60:
        print(f'{score}점은 합격입니다.')
    else:
        print(f'{score}점은 불합격입니다.')