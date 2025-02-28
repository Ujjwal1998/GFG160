def reverseList(head):
    prev = None
    curr = head
    while curr != None:
        n = curr.next
        curr.next = prev
        prev = curr
        curr = n
    return prev
