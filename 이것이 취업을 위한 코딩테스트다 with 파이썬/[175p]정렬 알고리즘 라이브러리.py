# 변수 선언
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array2 = [('바나나', 2), ('사과', 5), ('당근', 3)]

# sorted 소스 코드
result = sorted(array)
print(result)

# sort 소스 코드
array.sort()
print(array)

# key 활용 소스코드
def setting(data):
    return data[1]

result = sorted(array2, key=setting)
print(result)