# 이코테 298쪽

'''
N : 학생 (0번부터 N번)
M : 선생님이 하는 연산(union연산 or find연산)

입력
N, M
=> 0 a b : union 연산
=> 1 a b : find 연산 - 출력해야함
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

def team(stat, a, b):
    if stat == 0:
        union_parent(parent, a, b)
    elif stat == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            result.append("YES")
        else:
            result.append("NO")

N, M = map(int, input().split())
parent = [0] * (N+1)
result = []

for i in range(0, N+1):
    parent[i] = i

for _ in range(M):
    team(*map(int, input().split()))

for i in result:
    print(i)
