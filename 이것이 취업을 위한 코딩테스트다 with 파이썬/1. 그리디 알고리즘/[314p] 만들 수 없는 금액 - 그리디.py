# 이코테 314쪽

'''
N : 동전 개수
array : 화폐 단위

1~max값 까지
가장 큰 값부터 빼보고 만약 다 뺐는데 0이 아니면 그게 결과(빼는 것은 항상 자기보다 같거나 작은 수로)
'''
N = int(input())
array = list(map(int, input().split()))
array.sort(reverse=True)

for i in range(sum(array)):
    result = i
    for k in array:
        if i >= k:
            i -= k

    if i != 0:
        break

print(result)
