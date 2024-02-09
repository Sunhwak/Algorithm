num = -1
while num != 0 :
    a, b = map(int, input().split())
    num = a+b
    if num == 0 :
        break
    else :
        print(num)