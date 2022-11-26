import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    index = 0
    min_value = INF
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            index = i
            min_value = distance[i]
    return index

def dijkstra(start):
    # start Node 방문 처리 후 연결된 distance 정보 기록하기
    visited[start] = True
    distance[start] = 0
    for i in graph[start]:
        distance[i[0]] = i[1]

    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for i in graph[now]:
            cost = distance[now] + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost

dijkstra(start)
print(distance)


# 지금 궁금한 점 : 제일 적은 노드를 그때그때 방문 처리 하면 그 노드는 후에 더 작은 노드로 교체될 가능성은 없는지?
