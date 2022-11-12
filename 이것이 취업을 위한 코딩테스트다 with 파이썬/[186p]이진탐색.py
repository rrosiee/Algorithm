# 이코테 186쪽

## 순차 탐색 ##
'''def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

n, target = input().split()
n = int(n)
array = input().split()

print(sequential_search(n, target, array))


## 이진 탐색 ##
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

n, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search(array, target, 0, len(array))
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)'''

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

n, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search2(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)