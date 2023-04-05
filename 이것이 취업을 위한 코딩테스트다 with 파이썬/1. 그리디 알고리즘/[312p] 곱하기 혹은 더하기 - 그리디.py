# 이코테 312쪽

'''
S : 숫자로 이루어진 문자열
+ 또는 x를 왼쪽부터 차례대로 해서 가장 큰 수 구하기
'''

S = input()
result = 0

for i in S:
    if result==0 or int(i) == 0:
        result += int(i)
        print("<1>", result, int(i))
    else:
        result *= int(i)
        print("<2>", result, int(i))

print(result)