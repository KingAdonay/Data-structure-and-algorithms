from collections import deque
from typing import List, Optional

'''
    105. Construct Binary Tree from Preorder and Inorder Traversal
    
    Intuition:
    The first element in the preorder traversal is the root of the tree. We can find this root in the inorder traversal to determine the left and right subtrees.
    
    Approach:
    1. Use a queue to process the preorder traversal.
    2. Create a mapping of values to their indices in the inorder traversal for quick lookup.
    3. Recursively build the left and right subtrees by determining the boundaries in the inorder traversal based on the current root.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack, queue and the mapping
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_queue = deque(preorder)
        indices = {val: i for i, val in enumerate(inorder)}
        
        def helper(left_idx, right_idx):
            if right_idx < left_idx:
                return None
            
            val = preorder_queue.popleft()

            left = helper(left_idx, indices[val] - 1)
            right = helper(indices[val] + 1, right_idx)

            return TreeNode(val, left, right)

        
        return helper(0, len(inorder) - 1)

# Testcases:
solution = Solution()

def get_value_arr(node):
    if not node:
        return []

    return [node.val] + get_value_arr(node.left) + get_value_arr(node.right)

expected1 = solution.buildTree([3,9,20,15,7], [9,3,15,20,7])

assert get_value_arr(expected1) == [3,9,20,15,7]