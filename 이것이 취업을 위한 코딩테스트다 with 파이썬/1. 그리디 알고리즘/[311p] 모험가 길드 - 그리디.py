# 이코테 311쪽

'''
11122233
집합을 만들고 나면 삭제하자
그냥 똑같은 로직으로 해서 되면 +1, 안되면 0 이렇게 하고, INF를 사용하는게 좋을듯?
어디서부터 해야할지 애매하군??, replace를 활용하면 될 것 같은데?
'''

N = int(input())
array = list(map(int, input().split()))
array.sort()
INF = 100001
result = 0

# array를 한 번씩 돌리기
for i in range(N):
    # 현재 값보다 작거나 같은 값들(temp)의 개수가 현재 값보다 많다면,
    # 현재 값을 기준으로 집합으로 묶어주자.
    temp = [k for k in array if k <= array[i]]
    if array[i] <= len(temp):
        for k in temp[0:array[i]]:
            array.remove(k)
            array.append(INF)
        result += 1

print(result)