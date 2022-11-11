# 이코테 180p

N = int(input())
array = list()
for i in range(N):
    temp = input().split()
    array.append((temp[0], int(temp[1])))

array.sort(key=lambda array: array[1])
for i in array:
    print(i[0], end=' ')
