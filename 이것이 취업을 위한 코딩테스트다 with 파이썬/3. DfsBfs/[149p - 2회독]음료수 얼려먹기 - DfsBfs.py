N, M = map(int, input().split())
graph = list()
for _ in range(N):
    string = input()
    graph.append(list(map(int, [s for s in string])))

visited = [[False] * M for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
count = 0


def dfs(graph, x, y, visited):
    visited[x][y] = True
    for move_x, move_y in dir:
        # list를 벗어났는지 확인
        move_x = x + move_x
        move_y = y + move_y
        if not (0 <= move_x < N and 0 <= move_y < M):
            continue
        # 연결 되어있는지 확인
        if graph[move_x][move_y] != 0:
            continue
        # 방문 한건지(True) 안한건지 확인(False)
        if visited[move_x][move_y] is True:
            continue
        dfs(graph, move_x, move_y, visited)


for x in range(N):
    for y in range(M):
        if graph[x][y] == 0 and visited[x][y] is False:
            count += 1
            dfs(graph, x, y, visited)

print(count)
