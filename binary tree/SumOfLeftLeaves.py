from typing import Optional

'''
    404. Sum of Left Leaves
    Intuition:
    We can use a depth-first search (DFS) to traverse the binary tree and keep track of whether we are currently visiting a left child. 
    If we encounter a leaf node that is a left child, we can add its value to our sum.
    
    Approach:
    1. Define a helper function that takes the current node and a boolean indicating whether it is a left child as arguments.
    2. If the current node is None, return 0.
    3. Recursively call the helper function for the left and right children of the current node, passing True for the left child and False for the right child.
    4. If the current node is a leaf node (i.e., it has no left or right children) and it is a left child, return its value plus the sums from the left and right recursive calls.
    5. If the current node is not a leaf or not a left child, return just the sums from the left and right recursive calls.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack in the worst case (skewed tree).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], is_left = False) -> int:
        if not node:
            return 0
        
        res1 = self.dfs(node.left, True)
        res2 = self.dfs(node.right)

        if is_left and not node.left and not node.right:
            return node.val + res1 + res2
        
        return res1 + res2
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

# Testcases
solution = Solution()
# Testcase 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.sumOfLeftLeaves(root) == 24)
# Testcase 2
root = TreeNode(1)
print(solution.sumOfLeftLeaves(root) == 0)
# Testcase 3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(solution.sumOfLeftLeaves(root) == 4)