# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        def dfs(node:Optional[TreeNode]) -> Tuple[int,int]:
            if not node:
                return 0, 0

            left_path_sum, left_tilt_sum = dfs(node.left)
            right_path_sum, right_tilt_sum = dfs(node.right)

            tilt = abs(left_path_sum - right_path_sum)

            return node.val + left_path_sum + right_path_sum, tilt + left_tilt_sum + right_tilt_sum

        return dfs(root)[1]