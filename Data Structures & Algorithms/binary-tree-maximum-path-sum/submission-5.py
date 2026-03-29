# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathSum = float('-inf')

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            self.pathSum = max(self.pathSum, max(left + root.val, right + root.val, left + right + root.val, root.val))

            return root.val + max(left if left > 0 else 0, right if right > 0 else 0)

        dfs(root)
        return self.pathSum