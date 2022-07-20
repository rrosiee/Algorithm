N=int(input())
L=1
while N>L:
    N-=L
    L+=1
    
if L%2!=0:
    print("%d%s%d" %((L-N+1), '/', N))
else:
    print("%d%s%d" %(N, '/', (L-N+1)))