def reverse(head):
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def reverseKGroup(head, k):
    # Code here
    curr = head
    while curr is not None:
        kthNode = curr
        count = 0
        while count < k and kthNode:
            count += 1
            kthNode = kthNode.next
        if count == k:
            nextNode = kthNode.next
            kthNode.next = None
            newHead = reverse(curr)
            if newHead == kthNode:
                curr = newHead
            else:
                curr.next = newHead
        # for i in range(k-1):
        #     kthNode = kthNode.next
