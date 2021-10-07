#2908번 문제
example=input().split()
for i in range(len(example)):
    example[i]=example[i][2]+example[i][1]+example[i][0]
example=list(map(int, example))
print(max(example))