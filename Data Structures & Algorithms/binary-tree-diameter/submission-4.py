# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0
        def dfs(root, d):
            if not root:
                return 0

            left = dfs(root.left, d)
            right = dfs(root.right, d)
            d = max(left, right) + 1
            self.max_d = max(self.max_d, left + right)

            return d

        dfs(root, 0)
        return self.max_d


