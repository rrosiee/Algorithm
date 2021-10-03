import sys

for i in range(int(sys.stdin.readline())):
    print("Case #{}:".format(i+1), sum(map(int, sys.stdin.readline().split())))