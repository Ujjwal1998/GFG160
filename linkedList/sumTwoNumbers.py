class Solution:
    def reverse(self, head):
        curr = head
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def trimZeros(self, head):
        curr = head
        while curr is not None and curr.data == 0:
            # if curr.data == 0:
            curr = curr.next
        # else:
        # break
        return curr

    def addTwoLists(self, num1, num2):
        # code here
        num1 = self.trimZeros(num1)
        num2 = self.trimZeros(num2)
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)
        carry = 0
        d = Node(None)
        res = Node(None)
        d.next = res
        while num1 or num2 or carry != 0:
            currSum = carry
            if num1 is not None:
                currSum += num1.data
                num1 = num1.next
            if num2 is not None:
                currSum += num2.data
                num2 = num2.next
            res.next = Node(currSum % 10)
            carry = currSum // 10
            res = res.next
        return self.reverse(d.next.next)
