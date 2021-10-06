#1546번

N=int(input())
score=list(map(int, input().split()))
max_=max(score)

for i in range(len(score)):
    score[i]=(score[i]/max_)*100

print(sum(score)/len(score))