from typing import Optional

'''
    99. Recover Binary Search Tree
    
    Use DFS to find the two nodes that are swapped by comparing the current node with the previous node in the in-order traversal.
    
    Time Complexity: O(N) since we visit each node at most once
    Space Complexity: O(H) where H is the height of the tree, in the worst case O(N) if the tree is skewed
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prev = None, None, None

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node

            dfs(node.right)
        
        dfs(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val

# Testcases:
sol = Solution()
# Testcase 1
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.right = TreeNode(2)
sol.recoverTree(root1)
print(root1.val == 3 and root1.left.val == 1 and root1.left.right.val == 2)
# Testcase 2
root2 = TreeNode(3)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(2)
sol.recoverTree(root2)
print(root2.val == 2 and root2.left.val == 1 and root2.right.val == 4 and root2.right.left.val == 3)