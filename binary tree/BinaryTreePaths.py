from typing import List, Optional

'''
    257. Binary Tree Paths
    
    Intuition:
    We can use a depth-first search (DFS) to explore all paths from the root to the leaf nodes in the binary tree.
    As we traverse the tree, we can build the path string and add it to the result list when we reach a leaf node.
    
    Approach:
    1. Define a helper function that takes the current node and the path string built so far.
    2. If the current node is a leaf node, add the path to the result list.
    3. Recursively call the helper function for the left and right children of the current node, updating the path string accordingly.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node: Optional[TreeNode], path: str) -> None:
            if not node:
                return
            
            path = path + f'->{node.val}' if path else f'{node.val}'
            if not node.left and not node.right:
                res.append(path)
                return
            
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, '')

        return res
    
# Testcases:
solution = Solution()
print(solution.binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))) == ["1->2->5", "1->3"]) 
print(solution.binaryTreePaths(TreeNode(1)) == ["1"]) 