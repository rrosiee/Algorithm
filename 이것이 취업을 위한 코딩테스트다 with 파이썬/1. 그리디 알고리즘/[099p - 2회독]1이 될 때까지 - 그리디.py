'''
N : 자연수
K : 나눌 수 있는 수
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

이 두 가지 연산을 골라서 최소한만 연산해서 1로 만드는 것이 과제
'''

M, K = map(int, input().split())
first = M % K
second = (M - first) // K

result = first + second
print(result)
