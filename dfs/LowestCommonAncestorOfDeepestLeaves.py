from typing import Optional, Tuple

'''
    1123. Lowest Common Ancestor of Deepest Leaves
    
    Use DFS to find the depth of the deepest leaves and their lowest common ancestor.
    
    Compare the depth of the left and right subtrees at each node:
    - If they are equal, the current node is the lowest common ancestor of the deepest leaves, return the deepest depth and the current node.
    - If the left depth is greater, return the left depth and the left node.
    - If the right depth is greater, return the right depth and the right node.
    
    Time Complexity: O(N) since we visit each node at most once
    Space Complexity: O(H) where H is the height of the tree, in the worst case O(N) if the tree is skewed
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode], depth: int) -> Tuple[int, Optional[TreeNode]]:
            if not node:
                return 0, node
            
            if not node.left and not node.right:
                return depth, node
            
            left_depth, left_node = dfs(node.left, depth + 1)
            right_depth, right_node = dfs(node.right, depth + 1)

            if left_depth == right_depth:
                return left_depth, node
            elif left_depth > right_depth:
                return left_depth, left_node
            
            return right_depth, right_node
        
        _, ansestor = dfs(root, 0)

        return ansestor
    
# Testcases:
sol = Solution()
# Testcase 1
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(0)
root1.right.right = TreeNode(8)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
print(sol.lcaDeepestLeaves(root1).val == 2)
# Testcase 2
root2 = TreeNode(1)
print(sol.lcaDeepestLeaves(root2).val == 1)