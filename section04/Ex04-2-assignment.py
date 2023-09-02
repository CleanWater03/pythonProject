'''
파일명 : Ex04-2-assignment.py

대입 연산자
    변수에 값을 저장하기 위해 사용하는 연산자

print 형식 문자
    %d : 정수 데이터
    %f : 실수 데이터
    %o : 8진수 데이터
    %x : 16진수 데이터
    %s : 문자열 데이터
    %c : 문자 하나 데이터
'''
a, b = 10, 20
print('a = %d, b = %d ' % (a, b))

a, b = b, a # b를 a에 a를 b에 대입
print('a = %d, b = %d ' % (a, b))

'''
tmp = a
a = b
b = tmp
'''
a, b = b, a
print('a = %d')

'''
복합 대입 연산자
    +=
        ex) x += 3 -> x = x + 3 같다
    -=
        ex) x -= 3 -> x = x - 3 같다
'''
piggy_bank = 0
money = 10000
piggy_bank += money # piggy_bank = piggy_bank + 10000
print(f'저금통에 용돈 {money}원을 넣었습니다.')
print(f'저금통에 용돈 {piggy_bank}원을 넣었습니다.')

snack = 2000
piggy_bank -= snack # piggy_bank = piggy_bank - snack
print(f'저금통에서 스택 구입비 {snack}원을 뺐습니다.')
print(f'지금 저금통에는 {piggy_bank}원이 있습니다.')