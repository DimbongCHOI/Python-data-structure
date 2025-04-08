# ver2.1 - Linked List
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

    def len(self): # 길이 구하는 함수
        count = 0
        current = self.head
        while(current is not None):
            current = current.link
            count += 1
        return count

list1 = LinkedList()
list1.append(3)
list1.append(5)
list1.append(10)
list1.append(21)

list2 = LinkedList()
list2.append(4)
list2.append(6)
list2.append(15)
list2.append(26)
list2.append(33)

# 입력값 출력
print("Input:")
list1.printList()
list2.printList()

i, j = 0, 0
cur1 = LinkedList()
cur2 = LinkedList()
cur1 = list1.head
cur2 = list2.head
len1 = list1.len()
len2 = list2.len()

list3 = LinkedList()
while(i < len1 and j < len2):
    if(cur1.data < cur2.data):
        list3.append(cur1.data)
        cur1 = cur1.link
        i += 1
    else:
        list3.append(cur2.data)
        cur2 = cur2.link
        j += 1

while(i < len1):
    list3.append(cur1.data)
    cur1 = cur1.link
    i += 1
while(j < len2):
    list3.append(cur2.data)
    cur2 = cur2.link
    j += 1

# 최종 출력
print("Output:")
list3.printList()
