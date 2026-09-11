# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head):
        prev, curr, next = None, head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = ListNode()
        curr.next = head
        res = []

        while curr:
            temp = curr.next
            curr.next = None
            res.append(temp)
            for i in range(k):
                if i == 0:
                    curr = temp
                elif curr:
                    curr = curr.next
            
            # if curr:
            #     temp = curr.next
            #     curr.next = None
            #     curr = temp
                #cut connection

        #if there is a none at the end of the list that means we are good, if there is nothing
        #we dont touch the last node

        extra = res.pop()

        for i in range(len(res)):
            res[i] = self.reverseList(res[i])
            print(res[i].val)

        #we can stitch everything together now
        for i in range(len(res)-1):
            curr = res[i]
            while curr.next:
                #find tail
                curr = curr.next
            curr.next = res[i+1]

        curr = res[-1]
        while curr.next:
            curr = curr.next

        curr.next = extra

        return res[0]

        

            

    




