n, x = map(int, input().split())
listA = list(map(int, input().split()))

for ele in listA :
    if ele < x :
        print(ele, end = ' ')
    else :
        continue