n, m = map(int, input().split())

listA = [
    list(map(int, input().split()))
    for _ in range(n)
]

listB = [
    list(map(int, input().split()))
    for _ in range(n)
]

listC = [ [0 for _ in range(m)] for _ in range(n)]


for i in range(n) :
    for j in range(m) :
        listC[i][j] = listA[i][j] + listB[i][j]

for i in range(n) :
    for j in range(m) :
        print(listC[i][j], end = ' ')
    print()