from collections import deque
from typing import List, Optional

'''
    103. Binary Tree Zigzag Level Order Traversal
    
    Use BFS to traverse the tree level by level, and use a stack to reverse the order of nodes for every other level.
    
    Time Complexity: O(N) since we visit each node at most once
    Space Complexity: O(N) in the worst case if the tree is completely unbalanced, otherwise O(W) where W is the maximum width of the tree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        zigzag = []
        q =deque([root])

        while q:
            ans = []
            q_len = len(q)
            for _ in range(q_len):
                cur = q.popleft()
                ans.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            if len(zigzag) % 2 == 0:
                zigzag.append(ans)
            else:
                zigzag.append(ans[::-1])
        
        return zigzag

# Testcases
# Testcase 1: [3,9,20,null,null,15,7] -> [[3],[20,9],[15,7]]
# Testcase 2: [1] -> [[1]]
# Testcase 3: [] -> []