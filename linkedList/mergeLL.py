class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sortedMerge(head1, head2):
    # code here
    curr1 = head1
    curr2 = head2
    prev = Node(None)
    dummy = prev
    while curr1 and curr2:
        d1 = curr1.data
        d2 = curr2.data
        if d1 < d2:
            prev.next = curr1
            curr1 = curr1.next
        else:
            prev.next = curr2
            curr2 = curr2.next
        prev = prev.next
    if curr1 is not None:
        prev.next = curr1
    if curr2 is not None:
        prev.next = curr2
    return dummy.next
