st = input()

alp = 'abcdefghijklmnopqrstuvwxyz'

for a in alp :
    if a in st :
        print(st.index(a), end = ' ')
    else :
        print(-1, end = ' ')