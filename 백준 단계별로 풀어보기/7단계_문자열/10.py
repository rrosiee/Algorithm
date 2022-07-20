# 1316번 문제

sum_=0
for i in range(int(input())):
    ex=input()
    set_=set(ex)
    try:
        for i in range(0, len(ex)-1):
            if ex[i]!=ex[i+1]:
                set_.remove(ex[i])
        set_.remove(ex[len(ex)-1])
        sum_+=1
    except KeyError:
        sum_+=0
print(sum_)