# 이코테 327쪽 - (https://www.acmicpc.net/problem/3190)

# == 핵심 로직 == #
# 1. for문을 통해서 초를 늘리면서 탐색
# 2. 가다가 사과가 있으면 뱀의 몸 길이를 늘리고
# 3. 가다가 방향 지시가 있으면 방향을 바꾼다.
# 4. 그러다가 "보드를 벗어나거나", "몸통과 부딪히는" 경우 초를 반환한다.


# == 탐색 로직 == #
def execute():
    # == 보드 == #
    # N : 보드의 크기(N x N)
    N = int(input())

    # == 사과 == #
    # K : 사과의 개수
    K = int(input())
    # apple_set : 사과 set
    apple_set = {tuple(map(int, input().split())) for _ in range(K)}

    # == 뱀 == #
    # L : 뱀의 방향 전환 수
    L = int(input())
    # L_set : 뱀의 방향 변환 정보 set
    dir_set = set()
    for _ in range(L):
        X, C = input().split()
        dir_set.add((int(X), C))
    # 뱀 머리 방향
    dir = "RIGHT"
    # 뱀의 위치들
    snake = [(1, 1)]

    # 방향 전환 관련 변수
    dirs_D = {"RIGHT": "DOWN", "DOWN": "LEFT", "LEFT": "TOP", "TOP": "RIGHT"}
    dirs_L = {"RIGHT": "TOP", "TOP": "LEFT", "LEFT": "DOWN", "DOWN": "RIGHT"}
    moves = {"RIGHT": [0, 1], "DOWN": [1, 0], "LEFT": [0, -1], "TOP": [-1, 0]}

    i = 0
    while True:
        #print("i는", i, "snake는", snake, "dir_set은", dir_set)
        # == 방향 전환하기 == #
        if (i, "D") in dir_set or (i, "L") in dir_set:
            if (i, "D") in dir_set:
                dir_set.remove((i, "D"))
                dir = dirs_D[dir]
            elif (i, "L") in dir_set:
                dir_set.remove((i, "L"))
                dir = dirs_L[dir]

        else:
            # == 이동하기 == #
            i += 1
            head = (snake[0][0] + moves[dir][0], snake[0][1] + moves[dir][1])
            snake = [head] + snake

            # == 게임 끝 == #
            if len(snake) != len(set(snake)):  # 자신의 꼬리에 부딪히는지
                return i
            for a, b in snake:  # 보드에서 벗어나는지
                if a > N or b > N or a < 1 or b < 1:
                    return i

            # == 꼬리 추가 or not == #
            if head in apple_set:  # 사과 o
                apple_set.remove(head)

            elif head not in apple_set:  # 사과 x
                snake.pop(len(snake) - 1)


print(execute())
