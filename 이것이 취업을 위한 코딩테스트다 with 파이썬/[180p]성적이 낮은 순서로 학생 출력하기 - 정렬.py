# 이코테 180p

N = int(input())
array = list()
for i in range(N):
    temp = input().split()
    array.append((temp[0], int(temp[1])))

def select(array):
    return array[1]

array.sort(key=select)
for i in array:
    print(i[0], end=' ')
