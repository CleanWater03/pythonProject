'''
파일명 : Ex10-1-method-string.py

메소드(method)
    특정 객체가 가지고 있는 함수를 의미한다.
    객체.메소드() 사용 가능

객체 - 실제로 존재하거나, 추상적으로 식별 할 수 있는 것을 말한다.
    속성 - 변수
    기능 - 메소드(함수)
'''
print("10자리 폭 왼쪽 정렬 '{:<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 '{:>10d}'".format(123))
print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))
print()
print("10자리 폭 왼쪽 정렬 채움문자 '{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움문자 '{:*>10d}'".format(123))
print("10자리 폭 가운데 정렬 채움문자 '{:*^10d}'".format(123))

# count() 메소드
s = '내가 그린 기린 그림은 목이 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
result = s.count('기린')
print(result)

s = 'best of best'
result = s.count('best', 5)
print(result)

# find() 메소드 - 위치한 인덱스 번호 반환
s = 'apple'
result = s.find('p')
print(result)

# 존재하지 않은 값 -1 반환
print(s.find('z'))

# index() 메소드 - fjnd 메소드와 같지만 문자열이 존재하지 않을 경우 ValueError 발생!
result = s.index('p')
print(result)
# result = s.index('z')
# print(result)

