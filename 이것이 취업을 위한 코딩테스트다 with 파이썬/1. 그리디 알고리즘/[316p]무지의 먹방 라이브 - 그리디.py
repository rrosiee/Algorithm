'''
foot_times : 음식을 모두 먹는데 필요한 시간이 음식의 번호 순서대로 들어있는 배열
k : 방송이 중단된 시간
'''


def solution(food_times, k):
    while True:
        for i in range(len(food_times)):
            if food_times[i] > 0:
                food_times[i] -= 1
                k -= 1
            if k == -1:
                return i + 1

