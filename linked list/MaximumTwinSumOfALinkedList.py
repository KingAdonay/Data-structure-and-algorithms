from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSumRecursive(self, head: Optional[ListNode]) -> int:
        self.curr = head
        return self.findMax(head)
    
    def findMax(self, head:Optional[ListNode]) -> int:
        if not head:
            return 0
        
        maxx = self.findMax(head.next)
        summ = self.curr.val + head.val
        self.curr = self.curr.next

        return max(maxx, summ)

    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next if slow else head
        
        return slow.next
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        mid_node = self.findMid(head)
        reversed_curr = self.reverseList(mid_node)
        maxx = 0
        while reversed_curr:
            summ = reversed_curr.val + curr.val
            maxx = max(maxx, summ)
            reversed_curr = reversed_curr.next
            curr = curr.next
        
        return maxx

# Tests
# Testcase 1: [1, 2, 3, 4], expected = 5