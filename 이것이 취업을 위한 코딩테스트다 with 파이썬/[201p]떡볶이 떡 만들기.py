# 이코테 201쪽
def tteokbokki(array, target):
    start = min(array)
    end = max(array)
    while start <= end:
        mid = (start + end) // 2
        total = sum([i - mid for i in array if i >= mid])
        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result

N, M = map(int, input().split())
array = list(map(int, input().split()))
print(tteokbokki(array, M))