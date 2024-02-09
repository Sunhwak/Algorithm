x = int(input())
n = int(input())

sum = 0
for _ in range(n) :
    money, num = map(int, input().split())
    sum += (money * num)

if x == sum :
    print('Yes')
else :
    print('No')