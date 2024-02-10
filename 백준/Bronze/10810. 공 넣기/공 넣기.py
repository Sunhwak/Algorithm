n, m = map(int, input().split())

listA = [0] * (n+1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for p in range(i, j+1) :
        listA[p] = k

for ele in listA[1:] :
    print(ele, end = ' ')