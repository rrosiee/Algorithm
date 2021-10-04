#4344번 문제

num=int(input())
for i in range(num):
    class_=list(map(int, input().split()))
    c=0
    for k in class_[1:]:
        if k>(sum(class_[1:])/class_[0]):
            c+=1
    print('%.3f%%'%float((c/class_[0])*100))