from typing import Optional, Tuple

'''
    110. Balanced Binary Tree
    Intuition:
    A binary tree is balanced if the height difference between the left and right subtrees of any node is no more than one.
    We can use a recursive approach to check if each subtree is balanced and calculate its height at the same time.
    
    Approach:
    1. Define a helper function that takes a node as input and returns a tuple containing a boolean indicating if the subtree rooted at that node is balanced and an integer representing the height of that subtree.
    2. If the node is None, it is balanced and has a height of 0, so return (True, 0).
    3. Recursively call the helper function for the left and right children of the node to get their balance status and heights.
    4. If either subtree is not balanced, then the current subtree is also not balanced, so return (False, 0).
    5. Check if the height difference between the left and right subtrees is greater than 1. If it is, then the current subtree is not balanced, so return (False, 0).
    6. If the subtree is balanced, return (True, height) where height is 1 plus the maximum of the left and right subtree heights.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack in the worst case (skewed tree).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, node: Optional[TreeNode]) -> Tuple[bool, int]:
        if not node:
            return (True, 0)
        
        is_left_balanced, left_height = self.helper(node.left)
        if not is_left_balanced:
            return (False, 0)
        
        is_right_balanced, right_height = self.helper(node.right)
        if not is_right_balanced:
            return (False, 0)
        
        is_balaced = abs(left_height - right_height) <= 1

        return (is_balaced, 1 + max(left_height, right_height))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_tree_balanced, _ = self.helper(root)
        return is_tree_balanced
    
# Testcases
sol = Solution()
# Testcase 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(sol.isBalanced(root))

# Testcase 2
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(sol.isBalanced(root) == False)