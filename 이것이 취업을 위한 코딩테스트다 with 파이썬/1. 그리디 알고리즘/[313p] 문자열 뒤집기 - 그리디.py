# 이코테 313쪽

'''
S : 0과 1로만 이루어진 문자열

그리디 조건 -> 0을 가진 집합, 1을 가진 집합으로 구분 짓고, 더 작은 값을 기준으로 뒤집음
'''
S = input()
current = int(S[0])
result = 0

for i in S:
    if current != int(i):
        current = int(i)
        result += 1

result = (result+1) // 2
print(result)