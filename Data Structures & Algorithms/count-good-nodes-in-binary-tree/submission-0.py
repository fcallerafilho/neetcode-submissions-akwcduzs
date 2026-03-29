# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0

        def dfs(root, currMax):
            if not root:
                return None

            if root.val >= currMax:
                self.cnt += 1
                currMax = root.val

            dfs(root.left, currMax)
            dfs(root.right, currMax) 

        dfs(root, root.val)
        return self.cnt