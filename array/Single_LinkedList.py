class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class SingleLinkedList: # 단일 연결 리스트
    def __init__(self):
        self.head = None

    def append(self, data): # 끝에 노드 추가
        ## 기본 Error 처리
        if(data is None): # 데이터 유효성 검사
            raise ValueError("data 값을 None으로 추가할 수 없습니다.")

        new_node = Node(data)
        if(self.head is None): # 비어있는 리스트 -> head 지정, 끝
            self.head = new_node
            return

        current = self.head
        while(current.link is not None): # 마지막 노드 찾아서
            current = current.link

        current.link = new_node # link에 연결

    def printList(self): # 전체 출력, traverse
        current = self.head
        while(current is not None):
            print(current.data, end = ' → ')
            current = current.link
        print("끝")

    def insert(self, index, data): # 삽입
        ## 기본 Error 처리
        if not isinstance(index, int): # 인덱스 타입 검사
            raise TypeError("index는 정수여야 합니다.")
        if(index < 0): # 인덱스 유효성 검사
            raise ValueError("index 값이 0 보다 작을 수 없습니다.")
        if(data is None): # 데이터 유효성 검사
            raise ValueError("data 값을 None으로 추가할 수 없습니다.")

        new_node = Node(data)
        # 맨 앞에 삽입
        if(index == 0):
            new_node.link = self.head
            self.head = new_node
            return

        # 중간 삽입
        current = self.head
        for _ in range(index - 1):
            if(current is None): # 범위 초과 검사
                raise IndexError("index가 리스트 길이를 초과합니다.")
            current = current.link

        new_node.link = current.link
        current.link = new_node

    def search(self, data): # 값 찾아 인덱스 반환
        ## 기본 Error 처리
        if(data is None): # 데이터 유효성 검사
            raise ValueError("data 값을 None으로 추가할 수 없습니다.")

        current = self.head
        index = 0 # 반환할 위치

        while(current is not None):
            if(current.data == data):
                return index
            current = current.link
            index += 1

        return -1 # 못 찾은 경우

    def delete(self, index): # 인덱스 위치 삭제
        ## 기본 Error 처리
        if not isinstance(index, int): # 인덱스 타입 검사
            raise TypeError("index는 정수여야 합니다.")
        if(index < 0): # 인덱스 유효성 검사
            raise ValueError("index 값이 0 보다 작을 수 없습니다.")

        if(self.head is None): # 빈 리스트일 경우
            return

        if(index == 0): # index가 0일 경우
            self.head = self.head.link
            return

        current = self.head
        for i in range(index - 1): # 삭제 전 인덱스까지 이동
            if(current is None or current.link is None): # 잘못된 인덱스 일 경우
                raise IndexError("index가 리스트 길이를 초과합니다.")
            current = current.link

        current.link = current.link.link # 다다음 링크해버리기

    def reverse(self): # 리스트 뒤집기
        prev = None
        current = self.head

        while(current is not None):
            temp = current.link
            current.link = prev
            prev = current
            current = temp

        self.head = prev

    def swap(self, index1, index2): # 두 인덱스 값 교환
        ## 기본 Error 처리
        if not isinstance(index1, int): # 인덱스1 타입 검사
            raise TypeError("index1은 정수여야 합니다.")
        if(index1 < 0): # 인덱스1 유효성 검사
            raise ValueError("index1 값이 0 보다 작을 수 없습니다.")
        if not isinstance(index2, int): # 인덱스2 타입 검사
            raise TypeError("index2는 정수여야 합니다.")
        if(index2 < 0): # 인덱스2 유효성 검사
            raise ValueError("index2 값이 0 보다 작을 수 없습니다.")

        if(index1 == index2): # 같은 인덱스일 경우
            return

        node1 = self.head
        for _ in range(index1):
            if(node1 is None):
                raise IndexError("index1이 리스트 길이를 초과합니다.")
            node1 = node1.link

        node2 = self.head
        for _ in range(index2):
            if(node2 is None):
                raise IndexError("index2가 리스트 길이를 초과합니다.")
            node2 = node2.link

        if(node1 is not None and node2 is not None):
            (node1.data, node2.data) = (node2.data, node1.data)
