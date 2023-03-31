# 이코테 87p

N = int(input())
result = 0

for coin in [500, 100, 10]:
    if N // coin > 0:
        result += N // coin
        N -= coin * (N // coin)

print(result)