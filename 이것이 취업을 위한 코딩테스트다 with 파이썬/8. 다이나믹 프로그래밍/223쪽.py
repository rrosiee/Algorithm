# Variables
N = int(input())
d = [0] * 1001

# Main
d[0], d[1] = 1, 1
if N > 1:
    for i in range(2, N + 1):
        d[i] = d[i - 1] + (d[i - 2] * 2)

print(d[N] % 796796)
