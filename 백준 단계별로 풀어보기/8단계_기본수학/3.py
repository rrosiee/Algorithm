# 백준 1193번 문제

ex=int(input())
n=1 # 현재 단계

while True:
    if ((n-1)*(n))//2<ex and ((n)*(n+1))//2>=ex:
        sum_=n+1
        pront=ex-(((n-1)*n)//2)
        if n%2==1:
            pront=(n+1)-pront
        print('{}/{}'.format(pront, sum_-pront))
        break
    n+=1