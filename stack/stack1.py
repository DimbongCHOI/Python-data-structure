# stack1.py - Stack 실습 코드
def stack_example():
    stack = []
    stack.append(1)
    stack.append(2)
    print(stack.pop())

%%writefile data-structure-practice/queue/queue1.py
# queue1.py - Queue 실습 코드
def queue_example():
    from collections import deque
    queue = deque()
    queue.append(1)
    queue.append(2)
    print(queue.popleft())

%%writefile data-structure-practice/search/search1.py
# search1.py - Search 실습 코드
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

%%writefile data-structure-practice/sort/sort1.py
# sort1.py - Sort 실습 코드
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

%%writefile data-structure-practice/tree/tree1.py
# tree1.py - Tree 실습 코드
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_example():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

%%writefile data-structure-practice/heap/heap1.py
# heap1.py - Heap 실습 코드
def heap_example():
    import heapq
    heap = []
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 2)
    print(heapq.heappop(heap))

%%writefile data-structure-practice/graph/graph1.py
# graph1.py - Graph 실습 코드
def graph_example():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    print(graph)

%%writefile data-structure-practice/hash/hash1.py
# hash1.py - Hash 실습 코드
def hash_example():
    my_dict = {'key': 'value'}
    print(my_dict['key'])
