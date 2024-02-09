n = int(input())

for j in range(n-1, -1, -1):
        print(' '*j, end = '')
        print('*' * (n-j))