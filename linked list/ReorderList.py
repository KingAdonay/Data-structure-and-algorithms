from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findMid(self, head: ListNode) -> ListNode:
        slow, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next if slow else head
        
        return slow
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        
        mid = self.findMid(head)
        second_half = self.reverseList(mid.next)
        mid.next = None

        curr = head
        while curr.next:
            node1 = second_half
            node2 = curr.next
            second_half = second_half.next
            node1.next = node2
            curr.next = node1
            curr = node2
        if second_half:
            curr.next = second_half
    
# Tests
# Testcase 1: [1, 2, 3, 4], expected: [1, 4, 2, 3]
# Testcase 2: [1, 2, 3, 4, 5], expected: [1, 5, 2, 4, 3]
