n = int(input())

score = list(map(int, input().split()))
m = max(score)

total = 0
for i in range(len(score)) :
    score[i] = score[i]/m * 100
    total += score[i]

average = total / n
print(average)