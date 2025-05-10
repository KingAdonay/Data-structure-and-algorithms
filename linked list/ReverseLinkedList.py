# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
            if curr == None:
                return None
            if curr.next == None:
                curr.next = prev
                return curr
            
            next_node = curr.next
            curr.next = prev

            return helper(curr, next_node)
        
        new_head = helper(None, head)

        return new_head

# Tests
# Testcase 1: [1,2,3,4,5], expected [5,4,3,2,1]
# Testcase 2: [1,2], expected [2,1]
# Testcase 2: [], expected []