max_num = 0

listA = []
count = -1
for i in range(9) :
    num = int(input())
    listA.append(num)
    if num > max_num :
        max_num = num

print(max_num)
print(listA.index(max_num)+1)