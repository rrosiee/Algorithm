n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 종료
    if x <= -1 or x > n or y <= -1 or y >= m:
        return False
    # 해당 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 재귀적으로 호출하기
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
