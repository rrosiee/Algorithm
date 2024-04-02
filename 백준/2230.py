# 문제
# A[1], A[2], ..., A[n]
# 차이가 m 이상이면서 제일 작은 경우 -> 다이나믹 프로그래밍

# Variables
n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]


# main Section
def get_min_num(n, m, array):
    min_num = 1000000001
    for i in range(0, n):
        for k in range(i, n):
            diff = abs(array[i] - array[k])
            if diff >= m:
                if min_num > diff:
                    min_num = diff
                    if min_num == m:
                        return min_num
    return min_num

# Result
result = get_min_num(n, m, array)
print(result)