# 1712번 문제
ex=list(map(int, input().split()))
if ex[2]<=ex[1]:
    print(-1)
else:
    print(int(ex[0]/(ex[2]-ex[1])+1))