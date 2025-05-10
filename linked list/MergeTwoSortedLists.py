# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                new_val = list1
                list1 = list1.next
            else:
                new_val = list2
                list2 = list2.next
            
            curr.next = new_val
            curr = curr.next
        
        curr.next = list1 if list1 != None else list2

        return head.next

# Tests
# Testcase 1: [1,2,4] [1,3,3,4] => [1,1,2,3,3,4,4]
# Testcase 2: [] [] => []
# Testcase 3: [] [0] => [0]