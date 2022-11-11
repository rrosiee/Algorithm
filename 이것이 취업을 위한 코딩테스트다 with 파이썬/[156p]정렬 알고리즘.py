## 선택 정렬 ##
def selection_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    print(array)

selection_sort([10, 9, 8, 7])
