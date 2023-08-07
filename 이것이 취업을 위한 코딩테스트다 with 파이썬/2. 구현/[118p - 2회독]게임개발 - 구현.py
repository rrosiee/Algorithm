'''
N, M = 세로, 가로
a, b, dir = 좌표a, 좌표b, 방향(0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽)

'''

# 입력 받기
N, M = map(int, input().split())
a, b, dir = map(int, input().split())
arr = list()
for _ in range(N):
    arr.append(input().split())

# 동서남북 이동 경로
EWSN = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}  # 북(0), 동(1), 남(2), 서(3)
no_move = 0
visited = [[a, b]]


# 회전했을 때의 방향(동, 서, 남, 북)과 이동할 위치 & 회전 방향 : 3 -> 2 -> 1 -> 0
def turn(num):  #
    if num == 0:
        return 3, EWSN[3]
    else:
        return num - 1, EWSN[num - 1]


while True:
    dir, move = turn(dir)
    a_move = a + move[0]  # 가로
    b_move = b + move[1]  # 세로
    if 0 > a_move >= M or 0 > b_move >= N or [a_move, b_move] in visited or arr[a_move][b_move] == 1:  # 맵을 벗어남
        no_move += 1
    else:
        a, b = a_move, b_move
        no_move = 0
        visited.append([a, b])

    if no_move == 4:
        a = a + (move[0] * (-1))
        b = b + (move[1] * (-1))
        no_move = 0
        if arr[a][b] == 1:
            break

print(len(visited))
