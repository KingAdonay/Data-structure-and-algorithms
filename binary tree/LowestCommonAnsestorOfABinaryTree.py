
from typing import Optional

'''
    236. Lowest Common Ancestor of a Binary Tree
    
    Intuition:
    The lowest common ancestor of a tree is the first node to have find both nodes as its children down the tree.
    So if we try finding both values down the tree and the first node to satisfy our condition will be lowest common ansestor.
    One thing to note here is that a node could be it's own parent so we need to check the node value againest the two nodes we are looking for.
    
    Approach:
    1. Create a helper function get_parents which will look for the node that satisfy our common parent condition, or search for each value down the tree.
    2. Call the method with root.
    
    Time complexity: O(n), n being the number of nodes
    Space complexity: O(n), n being the size of the stack for recursion.
'''
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_parents(node: 'TreeNode') -> Optional['TreeNode']:
            if not node:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node
            
            left_res = get_parents(node.left)
            right_res = get_parents(node.right)

            if left_res and right_res:
                return node
            
            return left_res if left_res else right_res

        return get_parents(root)

# Testcases:
sol = Solution()
print(sol.lowestCommonAncestor(TreeNode(3, TreeNode(5), TreeNode(1)), TreeNode(5), TreeNode(1)).val == 3)