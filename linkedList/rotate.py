# left rotate
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def rotate(head, k):
    # code here
    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1
    if k % length == 0:
        return head
    k = k % length
    tail.next = head
    tmp = head
    cnt = 1
    while cnt < k:
        tmp = tmp.next
        cnt += 1
    newHead = tmp.next
    tmp.next = None
    return newHead
