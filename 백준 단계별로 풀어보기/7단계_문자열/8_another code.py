example=input()
sum_=0
alphabet=['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for i in example:
    for k in alphabet:
        if i in k:
            sum_+=alphabet.index(k)+3

print(sum_)