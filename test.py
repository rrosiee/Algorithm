# aabbacccc

def solution(s):
    result = 10000000
    str_dict = dict()
    for i in range(1, len(s) // 2 + 1):  # 쪼개는 기준 (10개라면 1, 2, 3, 4, 5)
        idx = 0  # 하나씩 늘릴 예정
        pre = ""
        cnt = 1
        str_dict[i] = ""
        while idx < len(s):
            # 이전 문자열과 동일할 경우
            if (pre == s[idx:idx + i]):
                cnt += 1

            # 이전 문자열과 동일하지 않을 경우
            elif (pre != s[idx:idx + i]):
                str_dict[i] += str(cnt) + pre
                pre = s[idx:idx + i]
                cnt = 1

            # 문자열 쪼개기 끝나고 남은 것
            if (len(s) - (idx) < i):
                str_dict[i] += s[idx + 1:len(s)]

            # 마지막 문자열 합치기
            idx += i
            if idx >= len(s):
                str_dict[i] += str(cnt) + pre

        # 가장 축약된 문자열의 길이를 result로 반환
        for _, v in str_dict.items():
            result = min(len(v.replace("1", "")), result)

    return result


print(solution("xababcdcdababcdcd"))
