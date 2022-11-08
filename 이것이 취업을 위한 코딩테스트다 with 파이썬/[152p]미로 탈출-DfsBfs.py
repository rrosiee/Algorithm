# 이코테 152쪽 - (https://velog.io/@gabang2/%EC%9D%8C%EB%A3%8C%EC%88%98-%EC%96%BC%EB%A0%A4%EB%A8%B9%EA%B8%B0)

#### -- 입력 받기 -- ####
N, M = map(int, input().split())
maze = list()
visited = list()
stack = list()
for _ in range(N):
    temp = str(input())
    maze.append([int(i) for i in temp])
    visited.append([False for i in range(M)])

def dfs(index, maze, visited, stack):
    visited[index[0]][index[1]] = True
    while [len(maze)-1, len(maze[0])-1] not in stack:
        stack.append(index)
        count = 0
        for i in [[-1, 0], [0, 1], [0, -1], [1, 0]]:
            temp_index = [a + b for a, b in zip(index, i)]

            if temp_index[0] >= 0 and temp_index[0] < len(maze) and temp_index[1] >= 0 and temp_index[1] < len(maze[0]):
                if visited[temp_index[0]][temp_index[1]] == False and maze[temp_index[0]][temp_index[1]] == 1:
                    dfs(temp_index, maze, visited, stack)
                    continue
                else:
                    count += 1
        if count == 4:
            dfs(stack[len(stack)-1], maze, visited, stack)
    return stack

result = dfs([0, 0], maze, visited, stack)
print(result)