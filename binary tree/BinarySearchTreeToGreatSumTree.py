# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node:Optional[TreeNode], total:int) -> int:
            if not node:
                return total

            res1 = dfs(node.right, total)
            node.val += res1
            res2 = dfs(node.left, node.val)
            return res2

        dfs(root, 0)
        return root
        
            