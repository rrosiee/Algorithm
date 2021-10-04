#2562번
list_=[]
for i in range(9):
    list_.append(int(input()))

print(max(list_), list_.index(max(list_))+1, sep='\n')