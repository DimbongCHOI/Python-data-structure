# queue1.py - Queue 실습 코드
def queue_example():
    from collections import deque
    queue = deque()
    queue.append(1)
    queue.append(2)
    print(queue.popleft())
