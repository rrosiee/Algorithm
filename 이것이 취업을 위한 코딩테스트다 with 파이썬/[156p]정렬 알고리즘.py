'''
break : 조건문과 반복문 탈출
continue : 조건문 탈출
'''

## 선택 정렬 ##
def selection_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    print(array)

## 삽입 정렬 ##
def insertion_sort(array):
    for i in range(1, len(array)):
        for k in range(i, 0, -1):
            if array[k] < array[k-1]:
                array[k], array[k-1] = array[k-1], array[k]
            else:
                break
    print(array)

## 퀵 정렬 ##
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1) # 왼쪽 부분
    quick_sort(array, right+1, end) # 오른쪽 부분
    return array

## 파이썬의 장점을 살린 퀵 정렬 코드
def quick_sort_ver2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_ver2(left_side) + [pivot] + quick_sort_ver2(right_side)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(array, 0, len(array)-1))
print(quick_sort_ver2(array))
insertion_sort(array)
selection_sort(array) # 선택 정렬
print(sorted(array)) # 파이썬 내장 정렬 함수
