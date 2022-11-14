# 이코테 201쪽
def tteokbokki(array, target):
    start = min(array)
    end = max(array)
    while start <= end:
        mid = (start + end) // 2
        mid_value = sum([i - mid for i in array if i >= mid])
        if mid_value == target:
            return mid
        elif mid_value > target:
            start += 1
        elif mid_value < target:
            end -= 1
    return None

N, M = map(int, input().split())
array = list(map(int, input().split()))
print(tteokbokki(array, M))