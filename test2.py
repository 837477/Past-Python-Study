N = int(input('입력:'))
for i in range(N):
    for j in range(N):
        if j >= i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
