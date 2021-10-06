# 10809번 문제
# 소문자 'a'의 아스키코드: 97
# 소문자 'z'의 아스키코드: 122

S=input()
result=[]

for i in range(97, 123):
    if S in chr(i):
        result.append(S.index(chr(i)))
    else:
        result.append(-1)

print(result)
for i in result:
    print(i, end=' ')