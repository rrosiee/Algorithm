# 이코테 99쪽

'''문제
어떠한 수 N이 1이 될 때 까지 다음의 두 과정 중 하나를 반복적으로 선택해 수행하려 함
단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있음
N에서 1을 뺀다.
N을 K로 나눈다.
N이 1이 될 때 까지 1번 혹은 2번의 과정을 수행해야하는 최소 횟수를 구하는 프로그램을 작성
'''


def mine():
    N, K = map(int, input().split())
    result = N % K
    N = N - result
    while N != 1:
        N = N / K
        result += 1
    print(result)


def book():
    n, k = map(int, input().split())
    result = 0
    while n >= k:
        while n % k != 0:
            n -= 1
            result += 1
        n //= k
        result += 1

    while n > 1:
        n -= 1
        result += 1

    print(result)


mine()
book()
