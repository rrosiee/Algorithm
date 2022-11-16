N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]
dx = [0] * 100

for i in range(1, M+1):
    temp = list()
    for k in money:
        if i-k >= 0:
            temp.append(dx[i-k] + 1)
    if len(temp) == 0:
        temp.append(0)
    dx[i] = min(temp)
print(dx[M])