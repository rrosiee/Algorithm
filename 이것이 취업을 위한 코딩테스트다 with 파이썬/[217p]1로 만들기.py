# 이코테 217쪽

dynamic = dict()

def make_one(number):
    if number % 5 == 0:
        a_5 = number // 5
        make_one(number // 5)
    if number % 3 == 0:
        a_3 = number//3
        make_one(number // 3)
    if number % 2 == 0:
        a_2 = number//2
        make_one(number // 2)
    make_one(number - 1)
    return number, a_5, a_3, a_2

print(make_one(26))