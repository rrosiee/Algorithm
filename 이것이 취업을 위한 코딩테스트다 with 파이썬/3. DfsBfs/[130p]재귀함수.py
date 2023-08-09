# 이코테 130p - (https://velog.io/@gabang2/%EA%BC%AD-%ED%95%84%EC%9A%94%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EA%B8%B0%EC%B4%88)

def factorial_iterative(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


print(factorial_iterative(5))
print(factorial_recursive(5))
