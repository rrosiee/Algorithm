word=str(input().lower())
alphabet=['abc','def','ghi', 'jkl','mno','pqrs','tuv','wxyz']
time=0
for a in word: #happy =>h
    for b in alphabet: #3번째 index
        if a in b:
            time+=alphabet.index(b)+3
print(time)