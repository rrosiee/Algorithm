'''
N : 행의 개수
M : 열의 개수
행을 선택하고 그 행에서 가장 낮은 카드를 뽑아야 하는데, 가장 큰 수를 뽑아야 한다.
'''

N, M = map(int, input().split())
array = list()

for _ in range(N):
    array.append(min(map(int, input().split())))

print(max(array))