from sys import stdin

# Variables
M, N, L = map(int, stdin.readline().split())
sadae = list(map(int, stdin.readline().split()))
animals = []
cnt = 0

for _ in range(N):
    animals.append(list(map(int, stdin.readline().split())))


def diff(s, x, y):
    diff = abs(s - x) + y
    if diff <= L:
        return True
    else:
        return False


for a in animals:
    for s in sadae:
        if diff(s, a[0], a[1]):
            cnt += 1
            break

print(cnt)
