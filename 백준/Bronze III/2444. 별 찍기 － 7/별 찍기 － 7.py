n = int(input())

for i in range(1, n) :
    print(' '*(n-i)+'*'*(i*2-1))

for i in range(n, -1, -1) :
    print(' '*(n-i)+'*'*(i*2-1))