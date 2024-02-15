st = input()

flag = False
for i in range(len(st)) :
    if st[i] == st[len(st)-i-1] :
        flag = True
    else :
        flag = False
        break

if flag :
    print(1)
else :
    print(0)