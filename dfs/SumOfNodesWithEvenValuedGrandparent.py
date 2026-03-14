# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        def helper(node, parents):
            if not node:
                return 0

            val = 0
            if len(parents) == 2 and parents[0] % 2 == 0:
                val = node.val

            parents.append(node.val)
            if len(parents) > 2:
                parents.pop(0)
            

            return val + helper(node.left, parents[:]) + helper(node.right, parents[:])

        return helper(root, [])