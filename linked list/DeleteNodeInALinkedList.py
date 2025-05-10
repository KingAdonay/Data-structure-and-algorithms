# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None
        while node.next:
            node.val = node.next.val
            prev = node
            node = node.next
        
        prev.next = None
    
# Tests
# Testcase 1: [2,0,1,3], node = 2, expected = [0,1,3]
# Testcase 1: [4,5,1,9], node = 1, expected = [4,5,9]