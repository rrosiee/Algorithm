# 1152번 문제

example=input().split()
for i in example:
    if i=='':
        example.remove('')
print(len(example))