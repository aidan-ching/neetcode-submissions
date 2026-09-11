# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #we reverse the second half of the list, then merge it with the first half

        #we can find the middle of the list using the fast and slow pointer method

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # print(slow.val)

        #second list
        list2 = slow.next
        #we split the two lists
        slow.next = None
        #reverse list2

        prev, curr, next = None, list2, None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        list2 = prev

        
        #now we merge head and list2

        curr = ListNode()
        newHead = curr

        while head and list2:
            curr.next = head
            head = head.next
            curr = curr.next
            curr.next = list2
            list2 = list2.next
            curr = curr.next

        if head:
            curr.next = head

        head = newHead.next

        






        