'''
파일명: Ex02-8-dict.py

Dictionary
    Key:Volue로 이루어져 쌍으로 데이터 값을 저장하는데 사용
'''

thisdict = {
    'brand':'나이키',
    'model':'Max90',
    'year': 1990
}
# 변수 하나에 데이터 저장
# 왼쪽이 key, 오른쪽이 데이터

# 키 이름을 사용하여 참조 할 수 있다.
# 값 가져오기
print(thisdict['brand'])
print(thisdict.get('model'))

# 키 목록 가져오기
print(thisdict.keys())

# 추가하기
thisdict = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1964
}
thisdict['color'] = 'RED'
print(thisdict)
thisdict.update({'bgColor':'black'})
print(thisdict)

# 변경하기
thisdict['color'] = 'Blue'
print(thisdict)
thisdict.update({'bgColor':'Yello'})
print(thisdict)
'''Red -> Blue, Blue -> Black으로 색 변경'''

# 항목 제거하기
thisdict.pop('model')
print(thisdict)

# 마지막 삽입된 항목 제거하기
thisdict.popitem()
print(thisdict)

