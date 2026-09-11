# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        if not root: return root

        queue.append(root)
        while queue:
            #pop first
            curr = queue.pop()

            #swap left and right
            curr.left, curr.right = curr.right, curr.left

            #append left and right if avaliable
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)

        return root