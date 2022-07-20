#2577번

A=int(input())
B=int(input())
C=int(input())

sum_=str(A*B*C)

for i in range(10):
    print(sum_.count(str(i)))
