'''
파일명 : Ex03-5-casting.py

형변환(casting)
    변수에 유형을 지정하려는 경우 캐스팅으로 가능.
'''
# 정수형
x = int(1)
print(x)
y = int(2.8)    # int 타입은 정수형이므로 소수점 값이 절삭 당함.
print(y)
z = int("3")    # 문자형 값도 정수로 변환됨.
z2 = "3"
print(z)
print(x+z)

# print(x + z2) => 오류 케이스
print(str(x) + z2)  # 정수형을 문자형으로 변환.
print(x + int(z2))  # 문자형을 정수형으로 변환.

# 실수형 - 소수점까지 출력됨.
x = float(1)
print(x)
z = float("3")
print(z)

# 문자형
x = str(1)  # "1"
y = str(2)  # "2"
print(x + y)    # 문자열 + 문자열 = 문자연결

# 아스키코드 변환
a = ord('A')
print(a)
b = chr(65)
print(b)