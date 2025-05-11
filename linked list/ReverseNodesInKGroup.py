# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        h = ListNode(0, head)
        g_prev = h
        curr = h.next
        count = 0

        while curr:
            count += 1

            if count == k:
                prev = g_prev.next
                reversing_node = prev.next
                for _ in range(k - 1):
                    next_node = reversing_node.next
                    reversing_node.next = prev
                    prev = reversing_node
                    reversing_node = next_node
                
                g_prev.next.next = reversing_node
                temp = g_prev.next
                g_prev.next = prev
                
                
                g_prev = temp
                count = 0
                curr = reversing_node
            else:
                curr = curr.next

        return h.next

# Tests
# Testcase 1: [1,2,3,4,5], k = 2 => [2,1,4,3,5]
# Testcase 2: [1,2,3,4,5], k = 3 => [3,2,1,4,5]
# Testcase 3: [1], k = 1 => [1]