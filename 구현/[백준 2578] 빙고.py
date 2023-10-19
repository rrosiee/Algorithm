# 백준 2578 (https://www.acmicpc.net/problem/2578)

# 문제 풀이 방법
# x판 있어야 한다 [[0, 0], [0,0]] 같은
# 12번째 부터 체크를 해보아야 한다. (제일 빨리 빙고가 될 경우)

# 완전 탐색 방법
# 1. 가로 -> 한 줄이 모두 1인지
# 2. 세로 -> 동일한 인덱스 [][여기] 의 원소가 모두 1인지
# 3. 대각선
# -> 대각선 1 : [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
# -> 대각선 2 : [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]


def paper_is_success(paper):
    cnt = 0  # 충족하는 줄 수

    # 가로로 확인하기
    for i in range(len(paper)):
        if paper[i].count(1) == 5:
            cnt += 1

    # 세로로 확인하기
    for i in range(len(paper[0])):
        if [paper[k][i] for k in range(len(paper))].count(1) == 5:
            cnt += 1

    # 대각선으로 확인하기 1 : ↙
    daegag1 = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
    cnt += 1
    for a, b in daegag1:
        if paper[a][b] != 1:
            cnt -= 1
            break
    # 대각선으로 확인하기 2 : ↗
    daegag2 = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    cnt += 1
    for a, b in daegag2:
        if paper[a][b] != 1:
            cnt -= 1
            break
    if cnt >= 3:
        return True
    elif cnt != 3:
        return False


def print_list(list_name):
    for i in list_name:
        print(i)

def get_answer_bingo_paper():
    bingo = list()
    for _ in range(5):
        bingo.append(list(map(int, input().split())))

    answer = list()
    for _ in range(5):
        answer += list(map(int, input().split()))

    paper = paper = [[0 for _ in range(5)] for _ in range(5)]

    return bingo, answer, paper

def solution():
    bingo, answer, paper = get_answer_bingo_paper()

    for i in range(len(answer)):
        for k in range(len(bingo)):
            try:
                paper[k][bingo[k].index(answer[i])] = 1
                if i + 1 >= 12:
                    # 3줄 충족하는지 확인 - 완전 탐색
                    if paper_is_success(paper):
                        return i+1
            except:
                continue

print(solution())