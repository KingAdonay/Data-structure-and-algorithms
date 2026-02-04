from typing import Optional

'''
    404. Sum of Left Leaves
    
    Intuition:
    A left leaf is a node that is a left child of its parent and has no children.
    We can perform a depth-first search (DFS) on the tree, checking if each node is a left leaf and summing their values.
    
    Approach:
    1. Define a helper function that takes a node as input.
    2. If the node is null, return 0.
    3. If the node has a left child that is a leaf, add its value to the sum.
    4. Recursively call the helper function on the left and right children of the current node and add their results to the sum.
    5. Return the total sum of left leaves.
    
    Time complexity: O(N) where N is number of nodes in the tree
    Space complexity: O(H) where H is height of the tree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        val = 0
        if node.left and not node.left.left and not node.left.right:
            val = node.left.val
        
        return val + self.dfs(node.left) + self.dfs(node.right)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    
# Testcases:
sol = Solution()
# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(sol.sumOfLeftLeaves(root1)) # 24  