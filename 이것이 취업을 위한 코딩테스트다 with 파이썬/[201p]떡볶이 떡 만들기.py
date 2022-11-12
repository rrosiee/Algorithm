# 이코테 201쪽
import numpy as np

N, M = map(int, input().split())
array = list(map(int, input().split()))

for i in range(max(array), -1, -1):
    temp = np.array(array) + np.array([-i] * len(array))
    temp[temp <= 0] = 0
    if sum(temp) >= M:
        print(i)
        break