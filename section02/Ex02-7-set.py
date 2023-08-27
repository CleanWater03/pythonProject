'''
파일명: Ex02-7-set.py

Set
    고유한 원소로 구성된 변경가능한 컬렉션 타입
    중복값을 허용하지 않는다.
    순서가 없다.
'''

thisset = {'피카츄', '라이츄', '파이리'}
# 실행 할 때 마다 순서가 변경된다.
print(thisset)

# 항목 가져오기
for x in thisset:   # thisset 길이만큼 반복
    print(x)

# thisset에 값 데려와서 x에 대입.
# 이후 출력.

# set 길이
print(len(thisset))

# 항목 가져오기
for x in thisset:   #thisset 길이만큼 반복
    print(x)

# 값이 있는지 확인
thisset = {'피카츄', '잠만보', '메타몽'}
print('피카츄' in thisset)
print('꼬부기' in thisset)

# 항목 추가하기
thisset.add('꼬부기')
print(thisset)

# 중복값 테스트 => 테스트 결과 중복값을 허용하지 않는다.
thisset.add('잠만보')
print(thisset)

# 다른 Set 항목 추가
thisset1 = {'피카츄', '라이츄', '파이리'}
thisset2 = {'꼬부기', '잠만보', '뮤츠'}
thisset1.update(thisset2)
print(thisset1)

# 항목 제거
thisset = {'피카츄', '라이츄', '파이리'}
thisset.remove('피카츄')
print(thisset)

# remove() - 없는 항목 삭제 시 에러 발생
# thisset.remove('피카츄')
# print(thisset)

thisset = {'피카츄', '라이츄', '파이리'}
thisset.discard('피카츄')
print(thisset)

# discard() 없는 항목 삭제 시 에러 발생하지 않는다.
thisset.discard('피카츄')
print(thisset)

# 항목 제거 방법2
thisset.pop()
print(thisset)

# 비우기
thisset.clear()
print(thisset)