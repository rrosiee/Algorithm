'''
"a" : 97
'''

loc_input = input()
loc = [ord(loc_input[0]) - 96, 9 - int(loc_input[1])]
cases = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

result = 0
for case in cases:
    if loc[0] + case[0] < 1 or loc[0] + case[0] > 8 or loc[1] + case[1] < 1 or loc[1] + case[1] > 8:
        print(case)
        continue
    result += 1

print(result)
