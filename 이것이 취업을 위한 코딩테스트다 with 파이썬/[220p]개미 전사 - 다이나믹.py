# 이코테 220쪽

N = int(input())
K = [0] + list(map(int, input().split()))

for i in range(2, N+1):
    K[i] = max(K[0:i-1]) + K[i]

print(max(K))