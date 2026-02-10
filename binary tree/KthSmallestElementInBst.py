from typing import Optional

'''
    230. Kth Smallest Element in a BST
    
    Intuition:
    The kth smallest element in a binary search tree (BST) can be found using an in-order traversal, which visits the nodes in sorted order.
    By keeping track of the count of nodes visited, we can identify when we have reached the kth smallest element.
    
    Approach:
    1. Perform an in-order traversal of the BST.
    2. Keep a count of the nodes visited during the traversal.
    3. Increment the count only when coming back from the left subtree (i.e., when we are visiting a node after visiting its left child).
    4. Pass the new count value to the right subtree.
    5. When the count equals k, return the value of the current node as it is the kth smallest element.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack in the worst case (skewed tree)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find_kth_min_node(node, cur_count):
            if not node:
                return node, cur_count

            left, l_count = find_kth_min_node(node.left, cur_count)
            if l_count == k:
                return left, l_count

            if l_count + 1 == k:
                return node, l_count + 1

            return find_kth_min_node(node.right, l_count + 1)

        kth_min_node, count = find_kth_min_node(root, 0)
        return kth_min_node.val if kth_min_node else 0
    
# Testcases:
solution = Solution()
print(solution.kthSmallest(TreeNode(3, TreeNode(1), TreeNode(4)), 1) == 1)
print(solution.kthSmallest(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6)), 3) == 4)