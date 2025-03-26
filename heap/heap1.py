# heap1.py - Heap 실습 코드
def heap_example():
    import heapq
    heap = []
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 2)
    print(heapq.heappop(heap))
