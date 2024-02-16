alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

st = input()

for i in alphabet :
    st = st.replace(i, '*')
print(len(st))