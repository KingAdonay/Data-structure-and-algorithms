from typing import Optional

'''
    129. Sum Root to Leaf Numbers
    Intuition:
    To find the sum of all root-to-leaf numbers, we can use a depth-first search (DFS) approach to traverse the binary tree.
    As we traverse the tree, we can keep track of the current path from the root to the current node as a string.
    When we reach a leaf node, we can convert the path string to an integer and add it to our total sum.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(h) where h is the height of the tree for the recursive stack.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], path: str) -> int:
            if not node:
                return 0
            path = path + str(node.val)
            if not node.left and not node.right:
                return int(path)
            
            return dfs(node.left, path) + dfs(node.right, path)
            
        return dfs(root, '')

# Testcases
sol = Solution()
# Testcase 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(sol.sumNumbers(root) == 25) # 25

# Testcase 2
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
print(sol.sumNumbers(root) == 1026) # 1026