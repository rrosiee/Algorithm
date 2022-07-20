'''책 92쪽 문제'''

# N 입력 개수 / M 더하는 개수 / K 연속 개수(인덱스  기준)
# N개의 배열 입력(공백으로 구분)
# K는 M보다 작거나 같다

N, M, K = map(int, input().split())
input_array = list(map(int, input().split()))

for i in range(N-1):
    for k in range(i, -1, -1):
        if input_array[k] <= input_array[k+1]:
            input_array[k], input_array[k+1] = input_array[k+1], input_array[k]

i = 1
total_sum = 0
while i <= M:
    if i % (K+1) == 0:
        total_sum += input_array[1]
    else:
        total_sum += input_array[0]
    i += 1

print(total_sum)