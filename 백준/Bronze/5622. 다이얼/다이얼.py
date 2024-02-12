dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

st = input()
total = 0

for j in range(len(st)) :
    for i in dial :
        if st[j] in i :
            total += dial.index(i) + 3

print(total)