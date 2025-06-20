from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next if slow else head
        
        return slow.next if slow else head