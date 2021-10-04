#1110번 문제

import sys
a=sys.stdin.readline().rstrip()
b=a
i=0

while True:
    if len(a)==1:
        a='0'+a

    c=str(int(a[0])+int(a[1]))

    if len(c)==1:
        c='0'+c

    a=a[1]+c[1]
    i+=1

    if int(a)==int(b):
        break

print(i)