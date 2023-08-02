'''
배열이 주어졌을 때,
M 번 더하고, K번 연속만 더할 수 있음 => 가장 큰 수를 만들어야 함
'''
print("=====나의 풀이=====")
N, M, K = map(int, input().split())
array = list(map(int, input().split()))

sort_array = sorted(array, reverse=True)

first = sort_array[0]
second = sort_array[1]

time = M // (K + 1)
left = M % (K + 1)
result = (first * (left + time * K)) + (second * time)
print(result)

print("=====책의 풀이=====")
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

