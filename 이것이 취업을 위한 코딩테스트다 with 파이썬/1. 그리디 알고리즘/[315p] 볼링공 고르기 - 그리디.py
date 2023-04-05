# 이코테 315쪽

'''
N : 볼링공의 개수
M : 공의 최대 무게
array : 각 볼링공의 무게

-> 배열에서 2개를 골랐을 때 각 숫자가 달라야 함
-> 2중 for문을 돌리기
'''

N, M = map(int, input().split())
array = list(map(int, input().split()))
result = 0

for i in range(0, N):
    for k in range(i+1, N):
        if array[i] != array[k]:
            result += 1

print(result)
