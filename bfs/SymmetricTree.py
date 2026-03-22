# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        q = deque([root])

        while q:
            n = len(q)
            stack = []
            for i in range(n):
                cur = q.popleft()
                val = None
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
                    val = cur.val
                    
                if i < n // 2:
                    stack.append(val)
                elif stack:
                    if stack[-1] != val:
                        return False

                    stack.pop()
                        
                

        return True
            
        