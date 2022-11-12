# 이코테 186쪽 - (https://velog.io/@gabang2/%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89)

## 순차 탐색 ##
def sequential_search(n, target, array):
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
    print(result + 1)


## 이진 탐색 ver 2 ##
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

## 이진 탐색에서 빠르게 입력받는 방법 ##
'''input()함수를 이용하면 동작 속도가 느려져 시간 초과로 오답 판정을 받을 수 있음'''
import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)