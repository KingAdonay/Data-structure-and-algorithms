"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def dfs(node: 'root') -> int:
            if not node:
                return 0

            maxx = 0
            for child in node.children:
                maxx = max(maxx, dfs(child))

            return maxx + 1

        return dfs(root)
        