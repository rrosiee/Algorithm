# 자물쇠와 열쇠 - https://school.programmers.co.kr/learn/courses/30/lessons/60059


# 자물쇠 주변 0추가
def make_big_lock(lock):
    result = [[0 for _ in range(N + 2 * M - 2)] for _ in range(N + 2 * M - 2)]
    for i in range(N):
        for k in range(N):
            result[i + M - 1][k + M - 1] = lock[i][k]
    return result


# key주변 0추가
def make_big_key(key):
    result = [[0 for _ in range(N + 2 * M - 2)] for _ in range(N + 2 * M - 2)]
    for i in range(M):
        for k in range(M):
            result[i][k] = key[i][k]
    return result


# key를 회전하기
def rotate(key):
    return [list(l) for l in list(zip(*key[::-1]))]


# key를 상하좌우로 이동하기
def move_big_key(big_key_v, dir):
    # 좌 의 경우
    if (dir == "좌"):
        for i in big_key_v:
            i.append(i.pop(0))
    if (dir == "상"):
        big_key_v.append(big_key_v.pop(0))

    return big_key_v



# 현재 키와, 현재 자물쇠를 결합했을 때 열리는지 확인
def open_lock(key, lock, big_key_q):
    big_lock_q = make_big_lock(lock)
    for i in range(len(big_lock_q)):
        for k in range(len(big_lock_q)):
            big_lock_q[i][k] += big_key_q[i][k]

    print_list(big_lock_q)
    for i in range(len(key), len(key) + len(lock)):
        for k in range(len(key) - 1, len(key) + len(lock) - 1):
            if big_lock_q[i][k] == 0 or big_lock_q[i][k] == 2:
                return False

    return True


def print_list(list_name):
    print("=====================")
    for s in list_name:
        print(s)


def final(key, lock):
    big_lock_h = make_big_lock(lock)
    big_lock_len = len(big_lock_h)
    i=0
    for _ in range(4):
        big_key_h = make_big_key(rotate(key))
        for _ in range(big_lock_len):
            for _ in range(big_lock_len-len(key)+1):
                big_key_h = move_big_key(big_key_h, "좌")
                if open_lock(key, lock, big_key_h): return True
                i+=1
            big_key_h = move_big_key(big_key_h, "상")
            if open_lock(key, lock, big_key_h): return True
            i += 1
    print(i)
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]  # M x M
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]  # N x N
M = len(key)
N = len(lock)
a = move_big_key(make_big_key(key), "상")
print(final(key, lock))

