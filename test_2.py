s=input()
d=[-1]*26
for i in s:
    d[ord(i)-97]= s.index(i)

for i in d:
    print(i, end=' ')