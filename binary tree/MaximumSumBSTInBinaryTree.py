from typing import Optional, Tuple

'''

    1373. Maximum Sum BST in Binary Tree
    Intuition:
    We can use a depth-first search (DFS) to traverse the binary tree and determine if each subtree is a binary search tree (BST). 
    If a subtree is a BST, we can calculate its sum and update the maximum sum found so far.
    
    Approach:
    1. Define a helper function that takes the current node as an argument and returns a tuple containing whether the subtree is a BST, the sum of the subtree, the maximum value in the subtree, and the minimum value in the subtree.
    2. Recursively call the helper function for the left and right children of the current node.
    3. Check if the current subtree is a BST by comparing the maximum value of the left subtree and the minimum value of the right subtree with the current node's value.
    4. If the subtree is a BST, calculate its sum and update the maximum sum found so far.
    5. Return the appropriate values for the current subtree to be used in the parent calls.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0

        def helper(node: Optional[TreeNode]) -> Tuple[bool, int, int, int]:
            if not node:
                return True, 0, float('-inf'), float('inf')

            is_left_bst, left_sum, max_left, min_left = helper(node.left)
            is_right_bst, right_sum, max_right, min_right = helper(node.right)

            if is_left_bst and is_right_bst and max_left < node.val < min_right:
                new_sum = right_sum + left_sum + node.val
                self.max_sum = max(self.max_sum, new_sum)
                return True, new_sum, max(node.val, max_right), min(node.val, min_left)
            
            return False, 0, float('-inf'), float('inf')
        
        helper(root)
        
        return self.max_sum
    
# Testcases:
solution = Solution()
print(solution.maxSumBST(TreeNode(1, TreeNode(4, TreeNode(2), TreeNode(3)), TreeNode(3, None, TreeNode(5)))) == 8)
print(solution.maxSumBST(TreeNode(4, TreeNode(3, TreeNode(1), TreeNode(2)), TreeNode(6, TreeNode(5), None))) == 11)