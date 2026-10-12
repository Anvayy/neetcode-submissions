# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            
            p1 = node.left if node.left else None
            p2 = node.right if node.right else None

            node.right = p1
            node.left = p2

            dfs(node.right)
            dfs(node.left)

            return node

        return dfs(root)

            
        