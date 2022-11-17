# 이코테 257쪽

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input()) # n: 노드 개수
m = int(input()) # m: 간선 개수
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for line in graph[1:]:
    print(line[1:])