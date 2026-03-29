# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, currSum):
            if not root:
                return False

            currSum += root.val

            if not root.left and not root.right:
                if currSum != targetSum:
                    currSum -= root.val
                    return False
                else:
                    return True
                
            if dfs(root.left, currSum):
                return True
            if dfs(root.right, currSum):
                return True

            return False

        return dfs(root, 0)



            
            

            
                

