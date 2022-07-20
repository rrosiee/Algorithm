#입출력방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수
#있으므로input대신에 sys.stdin.readline을 사용하는 것이 좋다.

import sys

n=int(input())
c=[]
for i in range(n):
    a, b=(sys.stdin.readline().rstrip()).split()
    c.append(int(a)+int(b))

for i in range(len(c)):
    print(c[i])
