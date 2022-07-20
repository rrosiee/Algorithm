#3052번 문제
a=[]
for i in range(10):
    a.append(str(int(input())%42))
print(len(set(a)))