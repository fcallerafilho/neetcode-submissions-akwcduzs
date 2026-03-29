# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root, diameter):
            if not root:
                return (0, diameter)

            left, diameter = dfs(root.left, diameter)
            right, diameter = dfs(root.right, diameter)
            diameter = max(diameter, left + right)
            
            return ((1 + max(left, right)), diameter)

        return dfs(root, 0)[1]