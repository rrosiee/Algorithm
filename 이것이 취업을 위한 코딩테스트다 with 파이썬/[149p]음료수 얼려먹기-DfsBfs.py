# 이코테 149쪽 - (https://velog.io/@gabang2/DFSBFS)

from collections import deque

def input_data():
    N, M = map(int, input().split())
    icemaker = list()
    for i in range(N):
        icemaker.append([])
        temp = str(input())
        icemaker[i] = [int(i) for i in temp]
    return icemaker

def bfs(N, M, icemaker):
    icemaker[N][M] = 1
    queue = deque([[N, M]])

    while queue:
        current = queue.popleft()
        for i in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            if current[0] + i[0] >= 0 and current[0] + i[0] < len(icemaker) and current[1] + i[1] >= 0 and current[1] + i[1] < len(icemaker[0]):
                if icemaker[current[0] + i[0]][current[1] + i[1]] == 0:
                    icemaker[current[0] + i[0]][current[1] + i[1]] = 1
                    queue.append([current[0] + i[0], current[1] + i[1]])
    return icemaker
                
def exe():
    count = 0
    icemaker = input_data()
    for i in range(len(icemaker)):
        for k in range(len(icemaker[0])):
            if icemaker[i][k] == 0:
                count += 1
                icemaker = bfs(i, k, icemaker)
    print(count)

exe()