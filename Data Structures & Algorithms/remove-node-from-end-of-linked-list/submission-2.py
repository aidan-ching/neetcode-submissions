# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #count length then remove node

        #formula is length - n

        #stop right before length-n then delete

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        if count == 1:
            return None
        if count-n == 0:
            return head.next

        curr = head



        for i in range(count-n-1):
            curr = curr.next

        curr.next = curr.next.next if curr.next else None

    

        return head