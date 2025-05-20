# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        prev = dummy_node
        curr = head
        first_of_pair = None
        while curr:
            next_node = curr.next
            if first_of_pair:
                curr.next = first_of_pair
                first_of_pair.next = next_node
                prev.next = curr
                prev = first_of_pair
                first_of_pair = None
            else:
                first_of_pair = curr
            
            curr = next_node
        
        return dummy_node.next
    
# Tests
# Testcase 1: [1,2,3,4], expected = [2,1,4,3]
# Testcase 2: [1,2,3], expected = [2,1,3]