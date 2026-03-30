# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, vals):
            if not root:
                return vals

            dfs(root.left, vals)
            dfs(root.right, vals)
            vals.append(root.val)

            return vals
        return dfs(root, [])