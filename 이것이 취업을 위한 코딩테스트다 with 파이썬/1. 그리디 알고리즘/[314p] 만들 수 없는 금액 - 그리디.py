# 이코테 314쪽

'''
N : 동전 개수
array : 화폐 단위

-> max(array)까지 1부터 순차적으로 확인할 예정
-> 화폐 단위 중 가장 큰 값부터 빼기(뺄 수 있을 경우에만)
-> 뺄 수 있을만큼 뺐는데 0이 아닌 경우, 결과 값이 됨
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
