# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1:
            return None

        f = head
        for i in range(n):
            f = f.next



        s = head

        while f:
            print(s.val)
            f = f.next
            s = s.next

        #edge case when s is the start of the list
        if s == head:
            return s.next

        prev = head
        while prev.next != s:
            prev = prev.next

        prev.next = s.next

        return head

        

        