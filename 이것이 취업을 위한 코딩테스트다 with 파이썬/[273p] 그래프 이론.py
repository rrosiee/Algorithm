# 이코테 273쪽 - 서로소 집합 자료구조

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

# 값 초기화 하기
'''
v : 노드의 수
e : 합치기 연산 (Union)의 수
'''
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

# 합치기 연산 수행
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    print("패런트 출력: ", parent)

# 출력 - 집합 출력하기(루트노드가 같다면 같은 집합임)
print("집합 : ", end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

# 출력 - 부모 테이블 출력하기
print("부모 테이블 : ", end='')
for i in range(1, v+1):
    print(parent[i], end=' ')