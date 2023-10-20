# 프로그래머스 60061 (https://school.programmers.co.kr/learn/courses/30/lessons/60061)

import copy


# todo : 시간 초과 에러가 뜸

# 개선할 점
# 1. for문 돌릴 때 인덱스 말고 명시적으로 할 것
# 2. list 대신 set를 이용하기
# 3. 모든 경우의 수를 고려해서 "수학적 연산"을 해보기


def do_or_not(frame_one, frame_current):
    # == frame_temp에 수행했을 때의 값을 저장 == #
    # 삭제할 경우 (frame_one 4번째 원소 : 0)
    if frame_one[3] == 0:
        if frame_one[0:3] in frame_current:
            frame_temp = copy.deepcopy(frame_current)
            frame_temp.remove(frame_one[0:3])
        else:
            frame_temp = copy.deepcopy(frame_current)

    # 설치할 경우 (frame_one 4번째 원소 : 1)
    else:
        frame_temp = copy.deepcopy(frame_current)
        frame_temp.append(frame_one[0:3])

    # == frame_temp가 모든 조건을 만족하는지 확인 == #
    for frame_temp_one in frame_temp:
        # 기둥과 보 나누기
        bo_list = list()
        gidung_list = list()
        frame_temp_2 = copy.deepcopy(frame_temp)
        frame_temp_2.remove(frame_temp_one)
        for f in frame_temp_2:
            if f[2] == 1:
                bo_list.append([f[0], f[1]])
                bo_list.append([f[0] + 1, f[1]])
            if f[2] == 0:
                gidung_list.append([f[0], f[1] + 1])

        # 기둥일 경우 (frame_temp_one 3번째 원소 : 0)
        if frame_temp_one[2] == 0:
            if gidung_valid(frame_temp_one, bo_list, gidung_list) == False:
                return frame_current
        # 보일 경우 (frame_temp_one 3번째 원소 : 1)
        elif frame_temp_one[2] == 1:  #
            if bo_valid(frame_temp_one, bo_list, gidung_list) == False:
                return frame_current

        else:
            print("do_or_not : 4번째 원소는 0또는 1이어야 합니다.")
    return frame_temp


def gidung_valid(frame_temp_one, bo_list, gidung_list):

    # 1. 기둥은 바닥 위에 있다.
    if frame_temp_one[1] == 0:
        return True

    # 2. 기둥은 보의 한쪽 끝에 있다.
    if frame_temp_one[0:2] in bo_list:
        return True

    # 3. 기둥은 다른 기둥의 위에 있다.
    if frame_temp_one[0:2] in gidung_list:
        return True

    # 기준에 충족하지 않음
    return False


def bo_valid(frame_temp_one, bo_list, gidung_list):

    # 1. 한쪽 끝 부분이 기둥 위에 있다.
    if frame_temp_one[0:2] in gidung_list or [frame_temp_one[0] + 1, frame_temp_one[1]] in gidung_list:
        return True

    # 2. 양쪽 끝 부분이 다른 보와 동시에 연결되어있다.
    if frame_temp_one[0:2] in bo_list and [frame_temp_one[0] + 1, frame_temp_one[1]] in bo_list:
        return True
    return False


def solution(n, build_frame):
    frame_current = list()
    for frame_one in build_frame:
        frame_current = do_or_not(frame_one, frame_current)
    frame_current.sort()
    return frame_current


result = solution(5,
                  [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])

print("결과:", result)
print(result == [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1],
                 [4, 0, 0]])
