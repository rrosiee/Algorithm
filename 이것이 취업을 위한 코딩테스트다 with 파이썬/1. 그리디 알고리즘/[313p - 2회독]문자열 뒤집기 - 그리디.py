'''
S : 0과 1로만 이루어진 문자열
*할 수 있는 행동*
1. 모든 숫자 뒤집기
2. 연속된 숫자 단위 뒤집기
'''
from collections import Counter

S = input()
arr = list()
i = 0
while True:
    if i == 0 or S[i - 1] != S[i]:
        arr.append(S[i])
    i += 1
    if i >= len(S) - 1:
        break

count = Counter(arr)
result = min(count.values())
print(result)
