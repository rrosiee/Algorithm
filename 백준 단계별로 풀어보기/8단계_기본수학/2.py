# 백준 2292번 문제
ex=int(input())
pre=1
n=1
while True:
    if ex==1:
        print(1)
        break
    pre+=6*(n-1)
    cur=pre+6*n
    if pre<ex and cur>=ex:
        print(n+1)
        break
    n+=1