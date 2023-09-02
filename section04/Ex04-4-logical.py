'''
파일명 : Ex04-4-logical.py

논리 연산자
    관계 연산자와 함께 사용되는 연산자로

'''

a = 10
b = 0
print('{} > 0 and {} > 0 : {}'.format(a, b, a > 0 and b > 0))
print('{} > 0 or {} > 0 : {}'.format(a,b, a>0 or b>0))

print(True and True)
print(True or True)
print(True and False)
print(True or False)
print(False and False)
print(False or False)

print('not {} : {}'.format(a, not a))
print('not {} : {}'.format(b, not b))   # 0 -> False 인식