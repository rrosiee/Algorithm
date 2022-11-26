# 이코테 259쪽

import sys
input = sys.stdin.readline
INF = int(1e9)

# 입력받음
N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
X, K = map(int, input().split())

for i in range(1, N+1):
    graph[i][i] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in graph:
    print(i)

if graph[1][K] == INF or graph[K][X] == INF:
    print(-1)
else:
    print(graph[1][K] + graph[K][X])