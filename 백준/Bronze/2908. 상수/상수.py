listA = list(map(str, input().split()))
reversed_listA = []

for ele in listA :
    ele = ele[::-1]
    reversed_listA.append(int(ele))


print(max(reversed_listA))