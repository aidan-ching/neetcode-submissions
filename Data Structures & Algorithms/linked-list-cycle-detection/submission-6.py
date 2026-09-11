# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = d = head

        while s and d and d.next:
            s = s.next
            d = d.next.next
            if s==d:
                return True


        return False