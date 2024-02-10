n = int(input())

listA = list(map(int, input().split()))

find_num = int(input())

count_num = listA.count(find_num)
print(count_num)