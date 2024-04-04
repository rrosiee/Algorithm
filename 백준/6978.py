# 참고한 풀이 : https://velog.io/@toezilla/BOJ-6987-%EC%9B%94%EB%93%9C%EC%BB%B5-Python
from itertools import combinations
import sys
input = sys.stdin.readline

# 백트래킹
def dfs(depth):
    global  cnt

    if depth == 15:
        cnt = 1
        for sub in res:
            if sub.count(0) != 3:
                cnt = 0
                break
        return

    country1, country2 = games[depth]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        # 경기 진행
        res[country1][x] -= 1
        res[country2][y] -= 1

        # (country1, x) & (country2, y)에 대한 모든 경우의 수에 대해 완료
        dfs(depth + 1)

        # 완료 했으면 다시 되돌리기
        res[country1][x] += 1
        res[country2][y] += 1


answers = []
games = list(combinations(range(6), 2))
for _ in range(4):
    array = list(map(int, input().split()))
    res = [array[i:i+3] for i in range(0, 18, 3)]
    cnt = 0
    dfs(0)
    answers.append(cnt)

print(*answers)