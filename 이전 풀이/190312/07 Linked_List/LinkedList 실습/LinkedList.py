class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

    # def __del__(self):
    #     print(self.data, '삭제')

class List:
    def __init__(self):
        self.head = None
        self.tail = None # 끝을 가리키는 변수 추가
        self.size = 0

    def printlist(self):
        if self.head is None:
            print("비었다!")
        else:
            print(self.size, "[ ", end="")
            cur = self.head
            # cur.next is not None을 하면 마지막 노드는 프린트 되지 않고, 이 상태에서 다음 노드를 추가하는 작업을 하면 됨
            while cur is not None:
                print(cur.data, end=" ")
                cur = cur.next
            print("]")

    def insertlast(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            # cur = self.head
            # while cur.next is not None:
            #     cur = cur.next
            # cur.next = node
            self.tail.next = self.tail = node
        self.size += 1

    def insertfirst(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def deletelast(self):
        if self.head is None:
            print("비었따!")
        else:
            prev, cur = None, self.head
            while cur.next is not None:
                prev, cur = cur, cur.next
            if prev is None:
                self.head = self.tail = None
                del cur
            else:
                prev.next = None
                self.tail = prev
                del cur

    def deletefirst(self):
        if self.head is None:
            print("비었따!")
        else:
            cur = self.head
            if cur.next is None:
                self.head = self.tail = None
            else:
                self.head = cur.next
            del cur
            self.size -= 1

    def insertAt(self, idx, val):
        if self.head is None:
            self.insertfirst(val)
        elif idx >= self.size:
            self.insertlast(val)
        else:
            prev, cur = None, self.head
            for i in range(idx):
                prev = cur
                cur = cur.next

            if prev is None:
                self.insertfirst(val)
            else:
                node = Node(val)
                cur.prev = node
                node.prev = prev
                node.next = prev.next
                prev.next = node
            self.size += 1

    def deleteAt(self, idx):
        pass

