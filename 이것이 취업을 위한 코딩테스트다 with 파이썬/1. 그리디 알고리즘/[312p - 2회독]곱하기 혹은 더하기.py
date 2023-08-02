'''
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 x혹은 +연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램 작성
S = 0~9로만 이루어진 문자열
'''

S = list(map(int, list(input())))
result = S[0]
for i in range(1, len(S)):
    if S[i] <= 1 or result < 1:
        result += S[i]
    else:
        result *= S[i]
print(result)
