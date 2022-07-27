# 이코테 118p - 풀이 과정 : ()

N, M = map(int, input().split())
temp_character = list(map(int, input().split()))
character = dict()
character['location'], character['compass'] = [temp_character[0], temp_character[1]], temp_character[2]
compass = {0: {'direction': [0, 1], 'next': 3, 'back': [0, -1]}, 1: {'direction': [1, 0], 'next': 0, 'back': [-1, 0]},
           2: {'direction': [0, -1], 'next': 3, 'back': [0, 1]}, 3: {'direction': [-1, 0], 'next': 0, 'back': [1, 0]}}
land = list()
result = 1

for i in range(N):
    land.append(list(map(int, input().split())))

while True:
    character['compass'] = compass[character['compass']]['next']
    print(character['location'][0] + compass[character['compass']]['direction'][0])
    if 0 <= character['location'][0] + compass[character['compass']]['direction'][0] < M \
            and 0 <= character['location'][1] + compass[character['compass']]['direction'][1] < N \
            and land[character['location'][0] + compass[character['compass']]['direction'][0]][
        character['location'][1] + compass[character['compass']]['direction'][1]] == 0:
        print('zlkdf')
        character['location'][0] += compass[character['compass']]['direction'][0]
        character['location'][1] += compass[character['compass']]['direction'][1]
        result += 1
    else:
        print('dsfls')
        if 0 <= character['location'][0] + compass[character['compass']]['back'][0] < M \
                and 0 <= character['location'][1] + compass[character['compass']]['back'][1] < N \
                and land[character['location'][0] + compass[character['compass']]['back'][0]] \
                [character['location'][1] + compass[character['compass']]['back'][1]] == 0:
            character['location'][0] += compass[character['compass']]['back'][0]
            character['location'][1] += compass[character['compass']]['back'][1]
            result += 1
        else:
            break

print(result)
