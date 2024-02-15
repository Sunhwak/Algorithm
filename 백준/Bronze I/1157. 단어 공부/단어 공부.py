word = input().lower()
wordlist = list(set(word))
cnt = []

for ele in wordlist :
    count = word.count(ele)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2 :
    print('?')
else :
    print(wordlist[(cnt.index(max(cnt)))].upper())