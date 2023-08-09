from collections import deque

N, M = map(int, input().split())  # N: 세로 / M : 가로
arr = list()
for _ in range(N):
    arr.append(list(map(int, input())))
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs():
    queue = deque()
    queue.append([(0, 0)])
    arr[0][0] = 0
    result = 0
    while queue:
        ii = queue.popleft()
        result += 1
        for n, m in ii:  # m : 가로 & n : 세로
            temp = list()
            for move_y, move_x in dir:
                move_y = n + move_y  # 세로
                move_x = m + move_x  # 가로
                if not (0 <= move_y < N and 0 <= move_x < M):
                    continue
                if arr[move_y][move_x] == 0:
                    continue
                if move_y == N - 1 and move_x == M - 1:
                    return result - 1
                temp.append((move_y, move_x))
                arr[move_y][move_x] = 0

            queue.append(temp)


print(bfs())
