import sys
input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))

d = [0] * (N + 1)

for i in range(N + 1):
    for k in range(i - 1, -1, -1):
        new_team_score = max(students[k:i]) - min(students[k:i])
        d[i] = max(d[k] + new_team_score, d[i])

print(d[-1])