# 승과 패의 수가 같아야 한다.
# 모든 합은 30이 되어야 한다.
# 무의 합은 짝수여야 한다.

def is_available(array):
    first, mid,mid_count,  last = 0, 0, 0, 0

    country_sum = 0
    for i in range(len(array)):
        country_sum += array[i]

        if i % 3 == 0:
            first += array[i]
        elif i % 3 == 1:
            if array[i] != 0:
                mid_count += 1
            mid += array[i]
        elif i % 3 == 2:
            # Case 5 : 각 나라의 합은 5를 넘을 수 없다.
            if country_sum != 5:
                return 0
            country_sum = 0
            last += array[i]

    # Case 1 : 전체 합이 30이어야 한다.
    sum_30 = first + mid + last == 30

    # Case 2 : 승과 패의 수가 동일해야 한다.
    equal_first_last = first == last

    # Case 3 : 나 혼자 무승부만 할 수는 없다.
    mid_available = mid % 2 == 0 and mid_count != 1

    # Case 4 : 각 나라의 합은 5가 되어야 한다.

    if sum_30 and equal_first_last and mid_available:
        return 1
    return 0

result = []
for _ in range(4):
    array = list(map(int, input().split()))
    result.append(is_available(array))

for r in result:
    print(r, end=' ')