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
