import sys

for i in range(int(sys.stdin.readline())):
    a=list(map(int, sys.stdin.readline().split()))
    print("Case #{}: {} + {} = {}".format(i+1, a[0], a[1], sum(a)))