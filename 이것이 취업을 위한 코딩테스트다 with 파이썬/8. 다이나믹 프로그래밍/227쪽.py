# Python
import sys

# Variables
N, M = map(int, input().split())
coins = [int(input()) for _ in range(N)]
INF = sys.maxsize
d = [INF] * 10001

# Main Section
d[0] = 0
for i in range(0, M + 1):
    for c in coins:
        d[i + c] = min(d[i + c], d[i] + 1)

print(d[M] if d[M] != INF else -1)
