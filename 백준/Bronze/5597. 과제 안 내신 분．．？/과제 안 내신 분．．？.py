list_num = [0] * 31

for _ in range(28) :
    i = int(input())
    list_num[i] = 1

for i in range(1, len(list_num)) :
    if list_num[i] == 0 :
        print(i)