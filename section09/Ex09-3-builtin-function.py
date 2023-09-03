'''
파일명 : Ex09-3-builtin-function

enumerate() 함수
    List, Tuple, String 등 순서가 있는 자료형을 입력받으면
    인덱스 값을 포함하는 enumerate 객체를 돌려줍니다.
'''
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month, day in enumerate(months):
    print(f'{month+1}월 = {day}일')