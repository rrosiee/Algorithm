def search(lst, mode=0):
    m = len(lst)
    result = []
    for i in range(m):
        for j in range(m):
            if lst[i][j] == mode:
                result.append((j, i))

    return result


def rotate(lst):
    m = len(lst)
    zero_point_adjust = lambda x: (x[0] - lst[0][0], x[1] - lst[0][1])
    result = [list(map(zero_point_adjust, lst))]

    for _ in range(3):
        tmp = list()
        for x, y in result[-1]:
            tmp.append((-y, x))
        result.append(tmp)

    return result


def is_matching(key_lst, lock, lock_size, lx, ly, n):
    cnt = 0
    for kx, ky in key_lst:
        x, y = lx + kx, ly + ky
        if -1 < x < n and -1 < y < n:
            if lock[y][x] == 1:
                return False
            cnt += 1

    return lock_size == cnt


def full_matching(key_lst, lock_lst, lock, n, m):
    key_size, lock_size = len(key_lst[0]), len(lock_lst)
    if key_size < lock_size:
        return False

    for ly in range(-n, n * 2):
        for lx in range(-n, n * 2):
            for _key in key_lst:
                if is_matching(_key, lock, lock_size, lx, ly, n):
                    return True
    return False


def solution(key, lock):
    m, n = len(key), len(lock)
    key_lst = search(key, mode=1)
    key_lst = rotate(key_lst)
    lock_lst = search(lock, mode=0)

    if not lock_lst:
        return True

    return full_matching(key_lst, lock_lst, lock, n, m)