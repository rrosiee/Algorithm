# Function Section
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# Variables
n, target = map(int, input().split())
array = list(map(int, input().split()))

# Main Section
result = binary_search(array, target, 0, n - 1)
if not result:
    print('해당하는 원소가 없습니다.')
else:
    print(result + 1)
