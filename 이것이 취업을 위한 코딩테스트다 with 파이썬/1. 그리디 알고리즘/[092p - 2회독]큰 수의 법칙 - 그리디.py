# 이코테 92쪽

'''
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M 번 더하여 가장 큰 수를 만드는 법칙
특정 인덱스는 K번을 초과하여 다해질 수 없음

N : 배열의 크기
M : 숫자가 더해지는 횟수
K : 각 인덱스당 더해질 수 있는 횟수 
'''

N, M, K = map(int, input().split())
numbers = map(int, input().split())
numbers - list(numbers)
numbers = numbers.sort(reverse = True)
total = 0

print(numbers)
for i in numbers:
    if M >= K:
        total += i * K
        M -= K
    elif M < K:
        total += i * M
        M -= M
        break

print(total)
