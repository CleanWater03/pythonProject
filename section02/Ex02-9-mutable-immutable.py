'''
파일명: Ex02-9-mutable-immutable.py

mutable - 메모리 값이 변경이 가능한 객체
    리스트(list), 세트(set), 딕셔너리(dict) ... 등
'''
me = [1, 2, 3] # me라는 변수 선언
print(me)

me.append(4) # 4라는 값 추가
print(me)

'''
파이썬 프로그램 실행 시 PVM이라는 메모리 공간이 생성된다.
me라는 변수 공간에 1, 2, 3이 순차적으로 들어간다.
PVM은 두가지 영역으로 구분이 된다.
프로그램의 명령어가 실행되는 스택(Stack) 영역과 변수가 생성되는 힙(Heap) 공간으로 나뉜다.
me는 주소값을 0001로 알고 있기에 그에 맞는 주소값으로 가서 append가 가능하다.
따라서 수정이 가능한 개체로 볼 수 있다.
'''
me = [1, 2, 3]
print(me)
print(id(me))

me.append(4)
print(me)
print(id(me))

'''
immutable - 메모리 값 변경 불가
    정수(int), 실수(float), 문자열(str), 튜플(tuple)
'''
imme = 10
print(imme)

imme += 1 # imme = imme + 1
print(imme)
print(id(imme)) # imme 위치 확인
# 값을 변경한 것으로 보이지만, 메모리 상으로는 변경된 것이 아니다.
# 실제로는 새로은 주소값에 새로운 숫자가 들어간 것이다.

imme2 = 10
print(imme2)
print(id(imme2)) # imme2 위치 확인
# 같은 주소값으로 imme2를 새로 만든다.

print('================================')
# immutable의 특성은 메모리에 어떤 값이 생기면 그 값은 절대 변동되지 않는다.
# 변경이 된다면 메모리의 값을 바꾸는 것이 아니라 새로운 값을 새로운 메모리의 공간으로 생성한다.

# 튜플 id값 확인하기
thistuple = ('피카츄', '라이츄', '파이리')
print(thistuple)
print(id(tuple))
# casting(형변환) ['피카츄', '라이츄', '파이리']
thiscast = list(thistuple)
thiscast[1] = '잠만보'
thistuple = tuple(thiscast) # ('피카츄', '잠만보', '파이리')
print(thistuple)
print(id(thistuple))
# 새롭게 생성된 thistuple은 기존의 것과 아예 다른 객체이다.