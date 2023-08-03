'''
N : 모험가 수
arr : 모험가 공포도
'''

N = int(input())
arr = sorted(list(map(int, input().split())))
temp = list()
result = 0

while arr:
    temp.append(arr.pop())
    if max(temp) > len(temp):
        continue
    elif max(temp) == len(temp):
        temp = list()
        result += 1

print(result)
