# 백준 2292번 문제

n, k=int(input()), 0

while n>1: #2밑으로 내려갈 때까지 계속
    k+=1
    n-=6*k

print(k+1)