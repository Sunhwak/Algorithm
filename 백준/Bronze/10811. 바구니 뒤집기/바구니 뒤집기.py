n, m = map(int, input().split())

listA = [i for i in range(n+1)]

for _ in range(m) :
    i, j = map(int, input().split())
    tmp = listA[i:j+1]
    tmp.reverse()
    listA[i:j+1] = tmp

for ele in listA[1:] :
    print(ele, end = ' ')