# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.next.val != curr.val:
                curr=curr.next
            else:
                curr.next = curr.next.next
        
        return head
            

# Tests
# Testcase 1: [] => []
# Testcase 2: [2] => [2]
# Testcase 3: [2, 2, 3, 3, 4] => [2, 3, 4]