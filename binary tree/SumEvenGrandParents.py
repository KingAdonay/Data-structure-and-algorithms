from typing import Optional

'''
    1315. Sum of Nodes with Even-Valued Grandparent
    
    Intuition:
    We can use a depth-first search (DFS) to traverse the binary tree and keep track of the grandparent nodes. Whenever we encounter an even-valued grandparent, we can add the values of its grandchildren to our sum.
    
    Approach:
    1. Define a helper function that takes the current node and its parent and grandparent as arguments.
    2. If the grandparent is even-valued, add the values of the current node's children to the sum.
    3. Recursively call the helper function for the left and right children of the current node, passing the current node as the new parent and the old parent as the new grandparent.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.summ = 0

        def helper(node):
            if not node:
                return

            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        self.summ += node.left.left.val
                    if node.left.right:
                        self.summ += node.left.right.val
                if node.right:
                    if node.right.left:
                        self.summ += node.right.left.val
                    if node.right.right:
                        self.summ += node.right.right.val
            

            helper(node.left)
            helper(node.right)

        helper(root)
        
        return self.summ