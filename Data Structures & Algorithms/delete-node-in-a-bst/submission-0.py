# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinValue(self, root: Optional[TreeNode]):
        curr = root
        while curr and curr.left:
            curr = curr.left

        return curr
            
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = Solution.deleteNode(self, root.right, key)
        elif key < root.val:
            root.left = Solution.deleteNode(self, root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                minNode = Solution.findMinValue(self, root.right)
                root.val = minNode.val
                root.right = Solution.deleteNode(self, root.right, minNode.val)

        return root