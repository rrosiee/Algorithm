# Third Party
from sys import stdin
import sys
sys.setrecursionlimit(10 ** 6)

# Variables
N, M = map(int, stdin.readline().split())
graph = list()
for i in range(N):
    graph.append(list(map(int, stdin.readline().split())))


# Main
def dfs(x, y):
    if x >= N or y >= M or x < 0 or y < 0:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x - 1, y + 1)

        dfs(x, y - 1)
        dfs(x, y + 1)

        dfs(x + 1, y - 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)

        return True

    return False


# Result
result = 0
for i in range(N):
    for k in range(M):
        if graph[i][k] == 1:
            dfs(i, k)
            result += 1

print(result)
