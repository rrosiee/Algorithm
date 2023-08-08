'''
N : 공 개수
M : 최대 무게
balls : 공 무게 배열
'''

N, M = map(int, input().split())
balls = list(map(int, input().split()))

count = 0

for index_ball1 in range(0, len(balls) - 1):
    for index_ball2 in range(index_ball1, len(balls)):
        ball1 = balls[index_ball1]
        ball2 = balls[index_ball2]
        if ball1 != ball2:
            count += 1

print(count)
