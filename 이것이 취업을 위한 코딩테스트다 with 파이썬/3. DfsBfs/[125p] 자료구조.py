from collections import deque


def stack():
    stack = []
    stack.append(1)  # [1]
    stack.append(2)  # [1, 2]
    stack.append(3)  # [1, 2, 3]
    stack.pop()  # [1, 2]
    stack.append(4)  # [1, 2, 4]
    print(stack)


def queue():
    queue = deque()
    queue.append(5)  # [5]
    queue.append(2)  # [5, 2]
    queue.append(3)  # [5, 2, 3]
    queue.popleft()  # [2, 3]
    queue.append(4)  # [2, 3, 4]
    queue.popleft()  # [3, 4]

    print(queue)
    queue.reverse()
    print(queue)


stack()
queue()
