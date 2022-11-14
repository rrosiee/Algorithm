# 이코테 212쪽


## 탑 다운 방식 ##
d = [0] * 1000
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
print('탑 다운 방식 결과:', fibo(99))


## 보텀 업 방식 ##
t = [0] * 1000
t[1] = 1
t[2] = 1
n = 99

for i in range(3, n+1):
    t[i] = t[i-1] + t[i-2]
print('보텀 업 방식 결과:', t[n])