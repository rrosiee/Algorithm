from functools import reduce

'''python lambda 함수'''

def hap(x, y):
    return x + y
print(hap(10, 20))
print((lambda x, y : x+y)(10, 20))

# map 함수의 lambda => map(함수, 리스트)
print(list(map(lambda x:x**2, range(5))))

# reduce 함수의 lambda => reduce(함수, 시퀀스)
print(reduce(lambda x, y: x+(y * 2), [0, 1, 2, 3, 4, 5]))

# filter 함수의 lambda => filter(함수, 리스트)
print(list(filter(lambda x:x<5, range(40))))

# lambda 함수는 말 그대로 함수이며, [lambda 매개변수 : 표현식] 형식에서 표현식에 매개변수를 계속 넣는 형식
data = [[1, 2], [100, 200], [1, 2000]]
data.sort(key=lambda x:x[1], reverse=True)
print(data)