'''
파일명 : Ex03-1-escape.py

이스케이프 문자
    \t -> 탭
    \b -> 백스페이스
    \\ -> \
    \' -> 작은 따옴표
    \" -> 큰 따옴표
    \n -> 개행(줄바꿈)
'''
print('Hello \'World\'')   # 문자 작은 따옴표를 인식시키기 위해 이스케이프 문자 사용.
print("Hello\"World\"")
print('Hello "World"')
# 작은 따옴표로 문자열을 생성해서 큰따옴표를 문자로서 인식 가능.
# 반대의 경우도 가능하다.
print('*\n**\n**')
print('이름\t연락처\t주소')
print('제시카\t02-1234-5678\t서울특별시 종로구 효자동 123-12')