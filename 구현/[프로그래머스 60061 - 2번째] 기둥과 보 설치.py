# 프로그래머스 60061 (https://school.programmers.co.kr/learn/courses/30/lessons/60061)

# == 기둥의 조건 == #
# 1. 기둥은 바닥 위에 있다.
# 2. 기둥은 보의 한쪽 끝에 있다.(왼쪽, 오른쪽)
# 3. 기둥은 또 다른 기둥 위에 있다.

# == 보의 조건 == #
# 1. 보는 한쪽 끝 부분이 기둥 위에 있다.(왼쪽, 오른쪽 고려)
# 2. 보는 양쪽 끝 부분이 다른 보와 동시에 연결되어있다.

# == 전체 로직 == #
# 1. set를 이용하여 임의로 바꿔본 후 기준이 충족하면 바꾸는 것 유지, 기준이 충족하지 않으면 기존 상태로
# 2. impossible 함수를 이용하여 설치가 가능한지 아닌지 확인하기

# == 배운 점 == #
# 1. for문을 쓸 때 x, y, a, b와 같이 이해하기 쉬운 변수를 쓸 것
# 2. set를 쓰면 ~ in set 에서 시간 초과를 예방할 수 있다. => 참고 자료()


def impossible(result):
    GIDUNG = 0
    BO = 1

    for x, y, type in result:
        if type == GIDUNG:  # 기둥
            # 3가지 조건에 전부 부합하지 않으면 True 반환
            if y != 0 and (x - 1, y, BO) not in result and (x, y, BO) not in result and (
                    x, y - 1, GIDUNG) not in result:
                return True

        elif type == BO:  # 보
            # 1. 보는 한쪽 끝 부분이 기둥 위에 있다.
            if (x, y - 1, GIDUNG) not in result and (x + 1, y - 1, GIDUNG) not in result and (
                    (x - 1, y, BO) not in result or (x + 1, y, BO) not in result):
                return True

    return False


def solution(n, build_frame):
    result = set()

    for x, y, type, status in build_frame:
        item = (x, y, type)
        if status == 1:  # 설치
            result.add(item)
            t = impossible(result)
            if impossible(result):
                result.remove(item)

        elif item in result:  # 삭제
            result.remove(item)
            t = impossible(result)
            if t:
                result.add(item)

    result = list(map(list, result))
    result.sort()

    return result


print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0],
                   [1, 1, 1, 0], [2, 2, 0, 1]]))
