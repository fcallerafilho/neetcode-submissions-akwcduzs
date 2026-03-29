# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.tree = ''
        def dfs(root):
            if not root:
                self.tree += 'N,'
                return
            
            self.tree += str(root.val) + ','
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return self.tree
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(',')
        iterator = iter(values)
        
        def helper():
            val = next(iterator)
            if val == 'N':
                return None
            treeNode = TreeNode(int(val))
            treeNode.left = helper()
            treeNode.right = helper()
            return treeNode

        return helper()


        