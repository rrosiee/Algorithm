# 이코테 92쪽

'''
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M 번 더하여 가장 큰 수를 만드는 법칙
특정 인덱스는 K번을 초과하여 다해질 수 없음

N : 배열의 크기
M : 숫자가 더해지는 횟수
K : 각 인덱스당 더해질 수 있는 횟수 
'''

# 초기 값 셋팅
N, M, K = map(int, input().split())
array = list(map(int, input().split()))
result = 0
cnt = 0

# 첫 번째로 큰 값, 두 번째로 큰 값
array.sort()
first = array[N-1]
second = array[N-2]

# 첫 번째로 큰 값 * K + 두 번째로 큰 값 * 1 을 M번 반복
while True:
    if M == 0:
        break
    if cnt < K:
        result += first
        cnt += 1
    else:
        result += second
        cnt = 0
    M -= 1

print(result)