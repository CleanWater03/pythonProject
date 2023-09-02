'''
파일명 : Ex06-4-while4.py
'''
dan = 2
while dan <= 9: # dan : 2, n : 1 -> 2 x 1 = 2
                # n : 2 -> 2 x 2 = 4 ... 2 x 9 = 18
                # dan : 3, n : 1 -> 3 x 1 = 3
                # n : 2 -> 3 x 2 = 6 ... 3 x 9 = 27
                # ...
                # dan : 9, n : 1 -> 9 x 1 = 9 ... 9 x 9 = 81
                # dan : 10일 때 바깥쪽 while 종료
    n = 1
    while n <= 9:
        print(f'{dan} x {n} = {dan*n} ', end=' ')
        n += 1
    dan += 1
    print()