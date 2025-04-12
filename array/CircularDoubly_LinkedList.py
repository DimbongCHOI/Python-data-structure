class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.linkLeft = None  # 이전 노드
        self.linkRight = None  # 다음 노드

class CircularDoublyLinkedList: # 순회 이중 연결 리스트
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        pass  # 노드 추가

    def printForward(self):
        pass  # 순방향 출력

    def printBackward(self):
        pass  # 역방향 출력

    def insert(self, index, data):
        pass  # 특정 위치에 삽입

    def delete(self, index):
        pass  # 특정 위치 삭제

    def search(self, data):
        pass  # 값 찾기

    def reverse(self):
        pass  # 전체 순서 뒤집기
