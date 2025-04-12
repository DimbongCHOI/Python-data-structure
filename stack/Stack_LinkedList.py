# ver2 - stack/LinkedList
class Node: # Node class 선언
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedStack:
    def __init__(self, size = None):
        if(size is not None): # 유한 LinkedStack으로 size 받을 때, 에러 처리
            if not isinstance(size, int): # (1) 정수여야함
                raise TypeError("입력 시, size는 정수여야 합니다.")
            if(size <= 0): # (2) 0보다 커야함
                raise ValueError("입력 시, size는 0보다 큰 정수여야 합니다.")
        self.top = None # 맨 위 노드. head 역할
        self.count = 0 # 현재 노드 개수
        self.max = size # 최대

    def printStack(self):
        current = self.top
        print("top(맨 위)", end = ': ')
        while(current is not None):
            print(current.data, end = ' -> ')
            current = current.link
        print("맨 아래")

    def isStackFull(self):
        if(self.max is None): # 무제한 스택이면 Full 이라는 개념이 없음
            return False
        return self.count == self.max

    def isStackEmpty(self):
        return self.top == None # 비어있으면 None

    def push(self, val):
        if(self.isStackFull()): # 개수 제한 스택에서 걸린 상황
            print("Stack is Full!")
            return
        new_node = Node(val)
        new_node.link = self.top
        self.top = new_node
        self.count += 1 # 현재 노드 개수

    def pop(self):
        if(self.isStackEmpty()):
            print("Stack is Empty!")
            return None
        val = self.top.data # 현재 top의 데이터를 저장
        self.top = self.top.link
        return val
