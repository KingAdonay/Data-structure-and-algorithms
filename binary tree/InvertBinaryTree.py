from typing import Optional

'''
    226. Invert Binary Tree
    Intuition:
    Inverting a binary tree means swapping the left and right children of all nodes in the tree.
    We can use a recursive approach to traverse the tree and swap the children of each node.
    
    Approach:
    1. Define a helper function that takes a node as input and performs the inversion.
    2. If the node is None, return immediately.
    3. Recursively call the helper function for the left and right children of the node to invert the subtrees.
    4. After the recursive calls, swap the left and right children of the current node.
    5. The main function will call the helper function with the root node and return the root after the inversion is complete.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack in the worst case (skewed tree).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)

            node.left, node.right = node.right, node.left
        
        dfs(root)

        return root
    
# Testcases
sol = Solution()
# Testcase 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
inverted_root = sol.invertTree(root)
print(inverted_root.val)  # 4
print(inverted_root.left.val)  # 7
print(inverted_root.right.val)  # 2
print(inverted_root.left.left.val)  # 9
print(inverted_root.left.right.val)  # 6
print(inverted_root.right.left.val)  # 3
print(inverted_root.right.right.val)  # 1