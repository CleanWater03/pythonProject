'''
파일명 : Ex07-4-for-dict.py

for문과 dict
'''
eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'
}
for word in eng_dict:
    print('{}의 뜻 : {}'.format(word, eng_dict.get(word)))

eng_dict_keys = eng_dict.keys()
print(eng_dict_keys)

for key, value in eng_dict.items():
    print(f'Key: {key}, Value: {value}')