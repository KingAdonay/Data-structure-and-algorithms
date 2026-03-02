from typing import List, Optional

'''
    94. Binary Tree Inorder Traversal
    
    Intuition:
    Inorder traversal of a binary tree is defined as visiting the left subtree, then the root node, and finally the right subtree.
    We can achieve this using a recursive helper function that processes each node in the correct order.
    
    Approach:
    1. Define a helper function that takes a node as input.
    2. If the node is None, return immediately.
    3. Recursively call the helper function on the left child, then append the node's value to the answer list, and finally call the helper function on the right child.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack and the answer list
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(node: Optional[TreeNode]):
            if not node:
                return
            
            helper(node.left)
            ans.append(node.val)
            helper(node.right)
        
        helper(root)

        return ans
# Testcases:
solution = Solution()
expected1 = solution.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3))))
assert expected1 == [1, 3, 2]
expected2 = solution.inorderTraversal(None)
assert expected2 == []