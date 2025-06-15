
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        while curr and curr.next:
            if curr.next.val == curr.val:
                duplicate_val = curr.val
                while curr and curr.val == duplicate_val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        
        return dummy.next

# Testcases
# 1. [1,2,3,3,4,4,5] => [1,2,5]
# 2. [1,1,1,2,3] => [2,3]
# 3. [1,2,2] => [1]