from typing import Optional, Tuple

'''
    98. Validate Binary Search Tree
    Intuition:
    A binary search tree (BST) is a binary tree where for every node, the values of all the nodes in the left subtree are less than the node's value,
    and the values of all the nodes in the right subtree are greater than the node's value.
    We can use a recursive approach to check if each subtree of the binary tree satisfies the properties of a BST.
    Approach:
    1. Define a helper function that takes a node as input and returns a tuple containing a boolean indicating if the subtree
    rooted at that node is a BST, the minimum value in that subtree, and the maximum value in that subtree.
    2. If the node is None, it is considered a valid BST with minimum and maximum values of 0.
    3. Recursively call the helper function for the left and right children of the node to get their validity and min/max values.
    4. Check if the current node's value is greater than the maximum value of the left subtree and less than the minimum value of the right subtree.
    If it is not, then the current subtree is not a BST, so return (False, 0, 0). If the subtree is a BST, return (True, min_value, max_value) 
    where min_value is the minimum of the left subtree's minimum value and the current node's value,
    and max_value is the maximum of the right subtree's maximum value and the current node's value.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack in the worst case.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node.left and not node.right:
                return True, node.val, node.val
            
            if not node.left:
                is_right_valid, right_min, right_max = helper(node.right)
                return is_right_valid and right_min > node.val, node.val, right_max
            
            if not node.right:
                is_left_valid, left_min, left_max = helper(node.left)
                return is_left_valid and left_max < node.val, left_min, node.val
            
            is_left_valid, left_min, left_max = helper(node.left)
            if not is_left_valid:
                return False, 0, 0
            
            is_right_valid, right_min, right_max = helper(node.right)
            if not is_right_valid:
                return False, 0, 0
            
            is_valid = left_max < node.val < right_min

            return is_valid, left_min, right_max
        
        return helper(root)[0]
    
# Testcases
sol = Solution()
# Testcase 1
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(sol.isValidBST(root)) # True  

# Testcase 2
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(sol.isValidBST(root) == False)

# Testcase 3
root = TreeNode(1)
root.left = TreeNode(1)
print(sol.isValidBST(root) == False)