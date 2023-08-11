class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None



    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
