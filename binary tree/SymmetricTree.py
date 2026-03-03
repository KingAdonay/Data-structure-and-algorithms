from typing import Optional

'''
    101. Symmetric Tree
    Intuition:
    A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.
    We can use a recursive approach to compare the left and right subtrees of the root node and check if they are mirror images of each other.
    
    Approach:
    1. Define a helper function that takes two nodes as input and checks if they are mirror images of each other.
    2. If both nodes are None, they are mirror images, so return True.
    3. If one of the nodes is None and the other is not, they are not mirror images, so return False.
    4. If the values of the two nodes are not equal, they are not mirror images, so return False.
    5. Recursively call the helper function for the left child of the first node and the right child of the second node, and for the right child of the first node and the left child of the second node.
    6. The tree is symmetric if both recursive calls return True.
    
    Time complexity: O(n) where n is the number of nodes in the tree
    Space complexity: O(n) for the recursive stack.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(left_node: Optional[TreeNode], right_node: Optional[TreeNode]):
            if not left_node or not right_node:
                return left_node == right_node
            
            if left_node.val != right_node.val:
                return False
            
            return traverse(left_node.left, right_node.right) and traverse(left_node.right, right_node.left)
            
        
        return traverse(root.left, root.right)
    
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        left_stack, right_stack = [root.left], [root.right]
       
        while left_stack and right_stack:
            left, right = left_stack.pop(), right_stack.pop()
            if not left and not right:
                continue
            
            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            left_stack.append(left.right)
            left_stack.append(left.left)
            right_stack.append(right.left)
            right_stack.append(right.right)
            
        return not left_stack and not right_stack


# Testcases:
solution = Solution()
print(solution.isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))) ) == False)  
print(solution.isSymmetricIterative(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))) ) == False)  

# Testcase 2: [2,3,3,4,5,null,4] == Flase