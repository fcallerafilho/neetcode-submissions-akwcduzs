# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.unbalanced = False

        def dfs(root):
            if not root:
                return 0

            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            if leftHeight - rightHeight not in [-1, 0, 1]:
                self.unbalanced = True

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return False if self.unbalanced else True
