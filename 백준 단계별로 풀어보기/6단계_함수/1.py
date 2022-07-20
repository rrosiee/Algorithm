#15596번 문제

#def solve(a):
#a는 합을 구해야 하는 정수 n개가 저장되어 있는 리스트임.
#return에는 정수의 합

def solve(a):
    sum_=0
    for i in a:
        sum_+=i
    return sum_

a=[1, 2, 3, 4, 5]
solve(a)