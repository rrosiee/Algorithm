# 이코테 197쪽

## 이진탐색을 활용한 풀이 ##
def yes_or_no(array, target, start=0, end=None):
    if end == None:
        end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return "yes"
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"
    
def exe():
    N = int(input())
    A = sorted(list(map(int, input().split())))

    M = int(input())
    B = list(map(int, input().split()))
    
    for i in B:
        print(yes_or_no(A, i), end=' ')
    print()

exe()


## 계수 정렬을 활용한 풀이 ##
N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

array = [0] * 1000001
for i in A:
    array[i] += 1
for i in B:
    if array[i] != 0:
        print('yes', end=' ')
    else:
        print('no', end=' ')


## 집합 자료형 이용 ##
N = int(input())
A = set(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print('yes', end=' ')
    else:
        print('no', end=' ')