# 이코테 300p

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
    if max_line < C:
        max_line = C
    union_parent(parent, A, B)
    total += C

print(total - max_line)