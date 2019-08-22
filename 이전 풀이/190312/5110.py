import sys
sys.stdin = open("5110.txt")

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

    def insertAt(self, index, data):
        front, cur = None, self.head
        for i in range(index):
            front = cur
            cur = cur.next
        if front is None:
            self.insertfirst(data[0])
            self.insertAt(1, data[1:])

        else:
            for i in range(len(data)):
                node = Node(data[i])
                node.next = cur
                front.next = node
                front = node
                cur = node.next

    def print_list(self):
        cur = self.head
        result = []
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result

    # def insertAt(self, idx, val):
    #     if self.head is None:
    #         self.insertfirst(val)
    #     elif idx >= self.size:
    #         self.insertlast(val)
    #     else:
    #         prev, cur = None, self.head
    #         for i in range(idx):
    #             prev = cur
    #             cur = cur.next
    #
    #         if prev is None:
    #             self.insertfirst(val)
    #         else:
    #             node = Node(val)
    #             node.prev = prev
    #             node.next = prev.next
    #             prev.next = node
    #             cur.prev = node
    #         self.size += 1

for t in range(int(input())):
    length, suyul = map(int, input().split())
    S = []
    ans = List()
    for _ in range(suyul):
        S.append(list(map(int, input().split())))

    while S:
        new = S.pop(0)
        i = 0
        if ans.head is None:
            pass
        else:
            cur = ans.head
            while cur is not None:
                if cur.data > new[0]:
                    break
                cur = cur.next
                i += 1

        ans.insertAt(i, new)

    # cur = ans.tail
    # print(f"#{t+1}", end=" ")
    # for _ in range(10):
    #     print(cur.data, end=" ")
    #     cur = cur.prev
    # print()

    print(f"#{t+1}", end=" ")
    result = ans.print_list()
    for i in range(10):
        print(result[-1-i], end=' ')
    print()





    # cur = ans.head
    # while cur is not None:
    #     print(cur.data, end=" ")
    #     cur = cur.next
    # print()
















    # 망함
    # idx = 0
    # for s in S:
    #     for n in s:
    #         N.append([idx, n])
    #         idx += 1
    # cnt, i = 0, 0
    # while S:
    #     new = S.pop(0)
    #     idx = length * cnt
    #     for i in range(idx):
    #         if N[i][1] > new[0]:
    #             break
    #     else:
    #         if i > 0:
    #             i += 1
    #
    #     new_cnt = idx - i
    #     new_idx = i
    #     new_st = N[new_idx][0]
    #     while new_cnt > 0:
    #         if N[new_idx][0] >= new_st:
    #             N[new_idx][0] += length
    #         new_idx += 1
    #         new_cnt -= 1
    #
    #     for n in range(length):
    #         N[idx+n][0] = new_st+n
    #
    #     cnt += 1
    #
    # for n in N:
    #     ans[n[0]] = n[1]
    #
    # print(f"#{t+1}", end=" ")
    # for i in range(len(ans)-1, len(ans)-11, -1):
    #     print(ans[i], end=" ")
    # print()





    # 시간 초과 2
    # ans = S.pop(0) + [0] * length * (suyul - 1)
    # cnt = 1
    # while S:
    #     new = S.pop(0)
    #     for i in range(length*cnt):
    #         if ans[i] > new[0]:
    #             break
    #     else:
    #         i += 1
    #
    #     re = length * cnt - i
    #     j = re + 1
    #     while re > 0:
    #         idx = length * (cnt + 1) - j + re
    #         ans[idx] = ans[idx-length]
    #         re -= 1
    #
    #     for n in range(length):
    #         ans[n+i] = new[n]
    #
    #     cnt += 1
    #
    # print(f"#{t+1}", end=" ")
    # for i in range(len(ans)-1, len(ans)-11, -1):
    #     print(ans[i], end=" ")
    # print()



    # 시간 초과
    # for s in S:
    #     a, idx = 0, len(ans)
    #     while a < idx:
    #         if ans[a] > s[0]:
    #             break
    #         a += 1
    #
    #     ans.extend([""] * length)
    #     if a >= idx:
    #         for i in range(length):
    #             ans[i+a] = s[i]
    #
    #     else:
    #         for i in range(len(ans)-1, a+length-1, -1):
    #             ans[i] = ans[i-length]
    #
    #         for i in range(length):
    #             ans[a+i] = s[i]
    #
    # print(f"#{t+1}", end=" ")
    # for i in range(len(ans)-1, len(ans)-11, -1):
    #     print(ans[i], end=" ")
    # print()



