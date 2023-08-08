N = input()
index_half = int(len(N) / 2)

left = sum([int(i) for i in N[0:index_half]])
right = sum([int(i) for i in N[index_half: len(N)]])

if left == right:
    print("LUCKY")
else:
    print("READY")
