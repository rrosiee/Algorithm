# 이코테 118p - 풀이 과정 : ()

#### 입력받기 ####
N, M = map(int, input().split())
character = list(map(int, input().split()))
land = list()
compass = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
result = 1
for i in range(N):
    land.append(list(map(int, input().split())))

#### 계산하기 ####
while True:
    # 캐릭터를 왼쪽으로 회전
    character[2] = (character[2] + 3) % 4
    land[character[0]][character[1]] = 1
    front_character = [character[0] + compass[character[2]][0], character[1] + compass[character[2]][1]]
    back_character = [character[0] + (compass[character[2]][0] * -1), character[1] + (compass[character[2]][1] * -1)]

    if 0 <= front_character[0] < M and 0 <= front_character[1] < N \
            and land[front_character[0]][front_character[1]] == 0:
        character[0], character[1] = front_character[0], front_character[1]

    elif 0 <= back_character[0] < M and 0 <= back_character[1] < N \
            and land[back_character[0]][back_character[1]] == 0:
        character[0], character[1] = back_character[0], back_character[1]

    else:
        break

    result += 1

print(result)
