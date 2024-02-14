listA = list(map(int, input().split()))

correct = [1, 1, 2, 2, 2, 8]
tmp = [0] * 6

for i in range(len(listA)) :
    tmp[i] = correct[i] - listA[i]

for ele in tmp :
    print(ele, end = ' ')