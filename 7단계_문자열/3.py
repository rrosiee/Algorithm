# 10809번 문제
# 소문자 'a'의 아스키코드: 97
# 소문자 'z'의 아스키코드: 122

s=input()
d=[-1]*26
for i in s:
    d[ord(i)-97]= s.index(i)

for i in d:
    print(i, end=' ')