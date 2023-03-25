# 이코테 300p
'''
N : 집 수
M : 길 수
A, B, C : 집 A, 집 B, A와 B간의 유지 비용
크루스칼 알고리즘을 이용하여 최소 신장 트리를 만들고,
해당 신장 트리에서 가장 큰 유지비용이 드는 cost를 뺀다.
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
total = 0
max_line = 0
graph = []
parent = [0] * (N + 1)
for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))

graph.sort()

for C, A, B in graph:
    print(C, A, B)
    if find_parent(parent, A) == find_parent(parent, B):
        continue
    union_parent(parent, A, B)
    max_line = C
    total += C

print(total - max_line)