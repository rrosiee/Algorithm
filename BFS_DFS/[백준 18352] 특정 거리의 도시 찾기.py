# 이코테 339쪽(https://www.acmicpc.net/problem/18352)

# 경로탐색, 네트워크, 조합만들기
# DFS : 재귀함수 -> 쉽게 푸는 문제
# BFS : 선형 행렬, 큐 -> 어렵게 푸는 문제

from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)