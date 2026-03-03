from collections import deque
from typing import Optional

'''
    104. Maximum Depth of Binary Tree
    Intuition:
    The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
    We can use a breadth-first search (BFS) approach to traverse the tree level by level and keep track of the maximum depth encountered.   
    
    Approach:
    1. If the root is None, return 0 as the maximum depth.
    2. Initialize a queue to perform BFS and a variable to keep track of the maximum depth.
    3. Enqueue the root node along with its level (starting at 0).
    4. While the queue is not empty, dequeue a node and its level.
    5. If the dequeued node is not None, enqueue its left and right children along with their respective levels (current level + 1).
    6. Update the maximum depth variable with the maximum of the current maximum depth and the level of the dequeued node + 1.
    7. After the BFS is complete, return the maximum depth. 
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the queue in the worst case (when the tree is completely unbalanced).
    '''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def bfs(node: Optional[TreeNode]):
            max_height = 0
            q = deque([(node, 0)])
            while q:
                cur, level = q.popleft()
                if cur:
                    q.append((cur.left, level + 1))
                    q.append((cur.right, level + 1))

                    max_height = max(max_height, level + 1)
            
            return max_height
        
        return bfs(root)

# Testcases:    
solution = Solution()
# Testcase 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.maxDepth(root) == 3)
# Testcase 2
root = TreeNode(1)
root.right = TreeNode(2)
print(solution.maxDepth(root) == 2) 