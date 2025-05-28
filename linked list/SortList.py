from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findMid(self, head: ListNode) -> ListNode:
        slow = None
        fast = head
        while fast and fast.next:
            slow = slow.next if slow else head
            fast = fast.next.next
        
        return slow
    
    def merge(self, first_half: ListNode, second_half: ListNode) -> ListNode:
        dummy_node, list1, list2 = ListNode(), first_half, second_half
        curr = dummy_node
        
        while list1 and list2:
            if list2.val < list1.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        
        if list2:
            curr.next = list2
        
        return dummy_node.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.findMid(head)
        half_start = mid.next
        mid.next = None
        first_half, second_half = self.sortList(head), self.sortList(half_start)

        return self.merge(first_half, second_half)

# Tests
# Testcase 1: [4,2,1,3], expected: [1,2,3,4]
# Testcase 2: [], expected: []