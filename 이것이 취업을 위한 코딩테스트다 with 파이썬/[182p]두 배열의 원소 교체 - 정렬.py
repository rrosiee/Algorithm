# 이코테 182쪽

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

for i in range(0, K):
    if A[i] < B[-i-1]:
        A[i], B[-i-1] = B[-i-1], A[i]
    else:
        break

print(sum(A))