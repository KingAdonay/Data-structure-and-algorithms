from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head.next, head

        while fast and fast.next:
            fast = fast.next.next
            slow = head if not slow else slow.next

        half_start = self.reverseList(slow.next)
        
        second_head = half_start
        while second_head:
            if head.val != second_head.val:
                return False
            head = head.next
            second_head = second_head.next
        
        return True
    
    def helper(self, node: Optional[ListNode]) -> bool:
        if not node:
            return True
        
        ans = self.helper(node.next) and node.val == self.curr.val
        self.curr = self.curr.next

        return ans
    def isPalindromeRecursive(self, head: Optional[ListNode]) -> bool:
        self.curr = head
        
        return self.helper(head)
    

# Tests
# Testcase 1: [1,2,2,1], expected = True
# Testcase 2: [1,2,1], expected = True
# Testcase 3: [1,2], expected = False
# Testcase 4: [1], expected = True