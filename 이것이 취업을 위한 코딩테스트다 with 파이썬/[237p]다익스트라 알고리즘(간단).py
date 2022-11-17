# 이코테 237쪽

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # n: 노드, m: 간선
start = int(input()) # start: 시작 지점
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    index = 0
    min_value = INF
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
# 궁금한 것 : 이렇게 하면 0이나 1 됐을 때 막 무한 루프 빠지거나 그러지는 않는지?

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

print(distance)