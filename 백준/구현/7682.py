# 7682

# invalid
# 1. 첫 번째 사람이 O를 놓을 경우

# VALID
# 1. 세로, 가로, 대각선이 이어진 경우

# Function
def is_valid(x):
    return set(x) == {'X'} or set(x) == {'O'}


def valid_or_invalid(case):
    if case[0] == 'O':
        return 'invalid'
    board = [list(case)[i:i + 3] for i in range(0, 9, 3)]

    for i in range(0, 3):
        garo = board[i]
        sero = [board[k][i] for k in range(0, 3)]
        if is_valid(garo) or is_valid(sero):
            return 'valid'

    daegag1 = [board[i][i] for i in range(3)]
    daegag2 = [board[i][i] for i in range(2, -1, -1)]
    if is_valid(daegag1) or is_valid(daegag2):
        return 'valid'
    return 'invalid'


# Main
case = ''
case_list = []

while True:
    case = input()
    if case == 'end':
        break
    case_list.append(case)

for case in case_list:
    print(valid_or_invalid(case))
