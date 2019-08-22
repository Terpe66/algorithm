import sys
sys.stdin = open("5120.txt")

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertlast(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = self.tail = node
        self.size += 1

    def insertfirst(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insertAt(self, idx, val):
        if idx == 0:
            self.insertfirst(val)
            return
        elif idx == self.size:
            self.insertlast(val)
        else:
            cur = self.head
            prev = cur.prev
            for i in range(idx):
                prev = cur
                cur = cur.next
            if prev is None:
                self.insertfirst(val)
            else:
                node = Node(val)
                node.prev = prev
                node.next = prev.next
                prev.next = node
                cur.prev = node
            self.size += 1

    def output(self, idx):
        cur = self.head
        prev = cur.prev
        for i in range(idx):
            prev = cur
            cur = cur.next
        if idx == self.size:
            ret = prev.data + self.head.data
        else:
            ret = prev.data + cur.data
        return ret



for t in range(int(input())):
    N, box, cycle = map(int, input().split())

    tmp = list(map(int, input().split()))
    ans = List()

    for i in range(N):
        ans.insertAt(i, tmp[i])

    idx = 0
    while cycle > 0:
        idx += box
        if idx > ans.size:
            idx -= ans.size
        new = ans.output(idx)
        ans.insertAt(idx, new)
        cycle -= 1

    cur = ans.tail
    print(f"#{t+1}", end=" ")
    if ans.size >= 10:
        for _ in range(10):
            print(cur.data, end=" ")
            cur = cur.prev
    else:
        for _ in range(ans.size):
            print(cur.data, end=" ")
            cur = cur.prev
    print()