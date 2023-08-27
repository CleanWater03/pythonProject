'''
파일명: Ex02-5-list.py
List
    단일 변수에 여러 항목을 저장하는데 사용된다.
    List 항목 순서가 지정되고 변경 가능하며 중복값을 허용한다.
    List에는 다양한 데이터 유형이 포함될 수 있다.
'''
thislist = ['피카츄', '라이츄', '꼬부기']
print(thislist)
print(thislist[0])

# List 길이
print(len(thislist))    # len() 함수 리스트 길이

# List 데이터 유형
list1 = ['피카츄', '라이츄', '파이리']   # 문자열
list2 = [1, 2, 3, 4, 5]     # 숫자
list3 = [True, False, True]     # 논리연산자
list4 = ['abc', 34, False, 40]  # 혼용 가능.

# 항목 접근
thislist = ['피카츄', '라이츄', '파이리']
print(thislist[1])

# 변경
thislist[1] = '잠만보' #리스트 변경 선언(라이츄를 잠만보로)
print(thislist)

# 항목 변경 2개
thislist = ['피카츄', '라이츄', '파이리', '꼬부기', '버터풀', '야도란']
thislist[1:3] = ['울먹이', '메타몽']  # 라이츄와 꼬부기를 없애고 울먹이와 메타몽 대입.
print(thislist)

# 두번째 세번째 값을 하나의 값으로 변경
thislist = ['피카츄', '라이츄', '파이리', '꼬부기', '버터풀', '야도란']
thislist[1:3] = ['잠만보'] # 라이츄와 파이리를 잠만보 하나로 바꾸기.
print(thislist)

# 항목추가
thislist = ['피카츄', '라이츄', '파이리']
thislist.append('꼬부기')
print(thislist)

# 항목 추가 - 인덱스 번호로 추가(insert)
thislist = ['피카츄', '라이츄', '파이리']
thislist.insert(1,'잠만보')
print(thislist)

# 항목 값으로 제거
thislist = ['피카츄', '라이츄', '파이리']
thislist.remove('라이츄')  #라이츄 제거
print(thislist)

# 항목을 지정된 인덱스로 제거
thislist = ['피카츄', '라이츄', '파이리']
thislist.pop(2)
print(thislist)

# 마지막 값 제거
thislist = ['꼬부기', '버터풀', '야도란', '피존투']
thislist.pop()  # 입력하지 않으면 마지막 값 제거
print(thislist)

# 목록 삭제
thislist = ['피카츄', '라이츄', '파이리']
thislist.clear()    # 목록 전부 삭제
print(thislist)

# 확장
thislist = ['피카츄', '라이츄', '파이리']
thislist.extend(['버터풀', '잠만보']) # 버터풀, 잠만보 추가
print(thislist)

# 객체 삭제
# del thislist
# print(thislist)
# thislist가 제거되어서 찾을 수 없음.

