def cloneLinkedList(head):
    # code here
    if head is None:
        return None
    curr = head
    while curr is not None:
        newNode = Node(curr.data)
        newNode.next = curr.next
        curr.next = newNode
        curr = newNode.next

    curr = head
    while curr is not None:
        if curr.random is not None:
            nextNode = curr.next
            nextNode.random = curr.random.next
        curr = curr.next.next

    curr = head
    cloneHead = head.next
    currClone = cloneHead
    while currClone.next is not None:
        curr.next = curr.next.next
        currClone.next = currClone.next.next
        curr = curr.next
        currClone = currClone.next
    curr.next = None
    currClone.next = None
    return cloneHead
