# 이코테 303쪽

'''

N : 강의의 수
N개의 줄 : 강의 시간, 선수 과목, -1

'''

from collections import deque
import copy

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
times = [0] * (N+1)

for i in range(1, N+1):
    line = list(map(int, input().split()))
    times[i] = line[0]
    for q in line[1:-1]:
        graph[q].append(i)
        indegree[i] += 1

def topology_sort():
    result = copy.deepcopy(times)
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        
        for i in graph[now]:
            indegree[i] -= 1
            result[i] += times[now]
            if indegree[i] == 0:
                q.append(i)

    print('수강 시간결과')
    print(result)

topology_sort()
    