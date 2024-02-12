t = int(input())

for _ in range(t) :
    tmp = ''
    r, s = map(str, input().split())
    r = int(r)
    for st in s :
        tmp += st*r
    print(tmp)