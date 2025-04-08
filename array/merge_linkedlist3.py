# ver2.3 - Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if(self.head is None): # 비어있는 리스트 -> head 지정, 끝
            self.head = new_node
            return

        current = self.head
        while(current.link is not None): # 마지막 노드 찾아서
            current = current.link

        current.link = new_node # link에 연결

    def printList(self): # 출력 함수
        current = self.head
        while(current is not None):
            print(current.data, end = ' -> ')
            current = current.link
        print("끝")

    def merge(self, other):
        cur1 = self.head
        cur2 = other.head

        merged = LinkedList()

        while cur1 and cur2:
            if cur1.data < cur2.data:
                merged.append(cur1.data)
                cur1 = cur1.link
            else:
                merged.append(cur2.data)
                cur2 = cur2.link

        while cur1:
            merged.append(cur1.data)
            cur1 = cur1.link

        while cur2:
            merged.append(cur2.data)
            cur2 = cur2.link

        return merged

list1 = LinkedList()
for val in [3, 5, 10, 21]:
    list1.append(val)

list2 = LinkedList()
for val in [4, 6, 15, 26, 33]:
    list2.append(val)

list3 = list1.merge(list2)  # 클래스 내부 메서드 사용!

# 입력값 출력
print("Input:")
list1.printList()
list2.printList()

# 최종 출력
print("Output:")
list3.printList()
