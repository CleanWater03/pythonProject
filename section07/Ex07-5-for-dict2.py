'''
파일명 : Ex07-5-for-dict2.py

이름/국어/영어/수학
John/90/85/95
Emily/92/88/96
Michael/98/90/92
Jessica/88/82/78

문제
    위 데이터 하나의 변수로 만들어보세요.
    그 변수 위와 같이 출력해보세요.

강사님 풀이

students = [
    {'이름':'John', '국어':90, '영어':85, '수학':95}
    {'이름':'Emily', '국어':92, '영어':88, '수학':96}
    {'이름':'Michael', '국어':98, '영어':90, '수학':92}
    {'이름':'Jessica', '국어':88, '영어':82, '수학':78}
]
# 자바의 경우는 각 변수가 개행 되어있다.

# 테이블 헤더 출력
print('이름/국어/영어/수학')

# 각 학생의 성적 출력
for studnet in students:
    name = student['이름']
    kor = student['국어']
    eng = student['영어']
    math = student['수학']
    print(f'{name}/{kor}/{eng}/{math}')
'''

# 다른 출력 방법
# print(students[1])
# print(type(students[1]))
# print(students[1]['영어'])

'''    
# 위에 것을 풀어서 쓰기(students 정의 부분)
    list[
    dict1 = {'이름':'John', '국어':90, '영어':85, '수학':95}
    dict2 = {'이름':'Emily', '국어':92, '영어':88, '수학':96}
    dict3 = {'이름':'Michael', '국어':98, '영어':90, '수학':92}
    dict4 = {'이름':'Jessica', '국어':88, '영어':82, '수학':78}
    ]
'''

# 나의 풀이
result_dict = {
    'John':'90/85/95',
    'Emily':'92/88/96',
    'Michael':'98/90/92',
    'Jessica':'88/82/78'
}

# 테이블 헤더 출력
print('이름/국어/영어/수학')

# 각 학생의 성적 출력
for word in result_dict:
    print('{}/{}'.format(word, result_dict.get(word)))