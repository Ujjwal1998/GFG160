def findFirstNode(head):
    # code here
    fast = head
    slow = head
    while slow is not None and fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
