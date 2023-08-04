'''
N : 공간의 크기(N, N)
array : 움직이는 방향 L(-1, 0), R(1, 0), U(0, 1), D(0, -1)
'''

N = int(input())
array = input().split()
traveler = [1, 1]
LRUD = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D": [1, 0]}

for i in array:

    if (traveler[0] + LRUD[i][0]) < 1:
        continue
    elif (traveler[1] + LRUD[i][1]) < 1:
        continue
    elif (traveler[0] + LRUD[i][0]) > N:
        continue
    elif (traveler[1] + LRUD[i][1]) > N:
        continue
    else:
        traveler = [traveler[0] + LRUD[i][0], traveler[1] + LRUD[i][1]]
    print(i)
    print(traveler)

print(traveler[0], traveler[1])
