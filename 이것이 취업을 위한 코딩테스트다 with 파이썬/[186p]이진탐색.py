# 이코테 186쪽

## 순차 탐색 ##
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1
n, target = input().split()
n = int(n)
array = input().split()

print(sequential_search(n, target, array))