# 이코테 178p - ()

N = int(input())
list_ = list()
for i in range(N):
    list_.append(int(input()))

def insertion_sort(array):
    for i in range(1, len(array) + 1):
        for k in range(i-1, 0, -1):
            print(i, k-1, k)
            if array[k-1] <= array[k]:
                array[k], array[k-1] = array[k-1], array[k]
            else:
                break
    for i in array:
        print(i, end=' ')

insertion_sort(list_)