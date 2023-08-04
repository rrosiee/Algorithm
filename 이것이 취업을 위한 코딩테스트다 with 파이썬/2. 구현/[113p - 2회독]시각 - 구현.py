'''
정수 N이 입력되면 00:00:00부터 N:59:59 중 3을 하나라도 포함하는 모든 경우의 수를 구하여라
'''

N = int(input())
result = 0

for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if "3" in str(s) + str(h) + str(m):
                result += 1

print(result)
