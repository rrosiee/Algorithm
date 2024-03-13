# Variables
X = int(input())
d = [0] * 30001

# Main Section
for i in range(2, X + 1):
    # 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 5를 나누는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    # 3을 나누는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 2를 나누는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[X])
