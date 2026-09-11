# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [p]

        a = []
        b = []

        while stack:
            curr = stack.pop()
            if curr:
                a.append(curr.val)
                stack.append(curr.left)
                stack.append(curr.right)
            else:
                a.append(None)

        stack.append(q)

        while stack:
            curr = stack.pop()
            if curr:
                b.append(curr.val)
                stack.append(curr.left)
                stack.append(curr.right)
            else:
                b.append(None)

        return a==b


        
