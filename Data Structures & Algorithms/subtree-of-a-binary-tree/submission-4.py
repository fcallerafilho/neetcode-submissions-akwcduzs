# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, arr):
            if not root:
                return None
                
            dfs(root.left, arr)
            dfs(root.right, arr)
            arr.append(root.val)

            return arr
        
        tree = dfs(root, [])
        subtree = dfs(subRoot, [])

        for i in range(len(subtree)):
            if tree[i] != subtree[i]:
                return False

        return True