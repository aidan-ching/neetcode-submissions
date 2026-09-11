# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #run bfs + each layer just attach a depth int and add to it
        if not root: return 0
        queue = deque()
        queue.append((root, 1))

        res = 1

        while queue:
            curr = queue.popleft()
            #check this one against max
            res = max(res, curr[1])

            #add the children to the queue
            if curr[0].left: queue.append((curr[0].left, curr[1]+1))
            if curr[0].right: queue.append((curr[0].right, curr[1]+1))

        return res
