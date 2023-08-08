'''
N : 동전 수
만들 수 없는 최소값
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()  # 1, 1, 2, 3, 9

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)
