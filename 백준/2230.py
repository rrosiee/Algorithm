import sys
input = sys.stdin.readline

def solution(array, N, M):
    left, right = 0, 0
    answer = 2000000001

    while right < N:
        diff = array[right] - array[left]
        if diff < M:
            right += 1
        elif diff > M:
            answer = min(answer, diff)
            left += 1
        else:
            return diff
    return answer

N, M = map(int, input().split())
array = [int(input().rstrip()) for _ in range(N)]
array.sort()

print(solution(array, N, M))