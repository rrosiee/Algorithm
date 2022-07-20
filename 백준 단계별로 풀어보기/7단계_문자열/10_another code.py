sum_=0
for i in range(int(input())):
    ex=input()
    if list(ex)==sorted(ex, key=ex.find):#알파벳을 찾은 순으로 전부 배열한 리스트
        sum_+=1
print(sum_)