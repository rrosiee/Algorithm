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

def insertion_sort(array):
    for i in range(1, len(array)):
        for k in range(i, 0, -1):
            if array[k] < array[k-1]:
                array[k], array[k-1] = array[k-1], array[k]
            else:
                break
    print(array)

insertion_sort([10, 9, 4])
selection_sort([10, 9, 8, 7]) # 선택 정렬
print(sorted([10, 9, 8, 7])) # 파이썬 내장 정렬 함수
