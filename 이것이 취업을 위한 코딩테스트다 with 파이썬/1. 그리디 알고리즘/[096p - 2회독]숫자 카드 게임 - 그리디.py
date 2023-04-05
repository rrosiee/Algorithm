# 이코테 96쪽

'''
N : 행 개수
M : 열 개수

N x M 행렬 중에서 그 행의 가장 낮은 숫자를 기준으로 가장 큰 값을 찾아야 한다.

=> 가장 낮은 숫자를 뽑은 후 가장 큰 값을 찾아보자!
'''

N, M = map(int, input().split())
maxCard = 0
for _ in range(N):
    a = min(list(map(int, input().split())))
    if maxCard < a:
        maxCard = a

print(maxCard)