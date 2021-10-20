for i in range(int(input())):
    M, N, K=map(int, input().split())
    field=[[0]*(M+2) for j in range(N+2)]
    n=0
    for k in range(0,K):
        X, Y=map(int, input().split())
        field[Y+1][X+1]=1
    for a in range(1, M+2):
        for b in range(1, N+2):
            if field[b][a]==1:
                if field[b][a-1]==1 or field[b][a+1]==1 or field[b-1][a]==1 or field[b+1][a]==1:
                    field[b][a]=0
                else:
                    n+=1
    print(n)