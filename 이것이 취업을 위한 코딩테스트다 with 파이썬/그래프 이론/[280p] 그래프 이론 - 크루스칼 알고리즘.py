# 이코테 280쪽

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

v, e = map(int, input().split())
parent = [0] * (v+1)
edges = []
total = 0

for i in range(0, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort(reverse=False) # O(ElogE)

for edge in edges:
    if find_parent(parent, edge[1]) == find_parent(parent, edge[2]):
        continue
    union_parent(parent, edge[1], edge[2])
    print('노드 {}와 {}의 cost는 {}'.format(edge[1], edge[2], edge[0]))
    total += edge[0]
        
print("총 비용 :", total)