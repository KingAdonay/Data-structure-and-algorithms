from typing import Optional

'''
    1038. Binary Search Tree to Greater Sum Tree
    
    Intuition:
    We can use a depth-first search (DFS) to traverse the binary search tree in reverse order (right, node, left).
    As we traverse, we can keep a running total of the sum of the nodes we have visited so far.
    For each node, we can update its value to be the sum of its original value and the running total.
    
    Approach:
    1. Define a helper function that takes the current node and the running total as arguments.
    2. Recursively call the helper function for the right child of the current node, passing the current total.
    3. Update the current node's value by adding the running total to its original value.
    4. Recursively call the helper function for the left child of the current node, passing the updated total.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node:Optional[TreeNode], total:int) -> int:
            if not node:
                return total

            res1 = dfs(node.right, total)
            node.val += res1
            res2 = dfs(node.left, node.val)
            return res2

        dfs(root, 0)
        return root
        
#Testcases:
solution = Solution()
def get_value_arr(node):
    if not node:
        return []

    return get_value_arr(node.left) + [node.val] + get_value_arr(node.right) 
expected1 = solution.bstToGst(TreeNode(4, TreeNode(1), TreeNode(6)))
assert get_value_arr(expected1) == [11, 10, 6]