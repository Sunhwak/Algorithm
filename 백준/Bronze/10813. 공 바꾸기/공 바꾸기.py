n, m = map(int, input().split())

listA = []
for i in range(n+1) :
    listA.append(i)

for _ in range(m) :
    i, j = map(int, input().split())
    listA[i], listA[j] = listA[j], listA[i]

for ele in listA[1:] :
    print(ele, end = ' ')