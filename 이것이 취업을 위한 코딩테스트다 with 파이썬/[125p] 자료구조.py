from collections import deque


def stack():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.pop()
    stack.append(4)
    print(stack)


def queue():
    queue = deque()
    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.append(4)
    queue.popleft()

    print(queue)
    queue.reverse()
    print(queue)


stack()
queue()
