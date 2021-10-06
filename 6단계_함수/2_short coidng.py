import sys

def d(n:int):
    return n+n//1000+(n%1000)//100+(n%100)//10+n%10

dList=[0]*10000

for n in range(10000):
    try:
        dList[d(n)]=1
    except IndexError:
        continue

for d in range(10000):
    if dList[d]==0:
        print(d)