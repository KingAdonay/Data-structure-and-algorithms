from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        h = head
        while h:
            sz += 1
            h = h.next

        if sz == n:
            return head.next
        
        h = head
        for _ in range(sz - n - 1):
            h = h.next
        
        if h.next:
            h.next = h.next.next
        else:
            h.next = None

        return head
    
    def removeNthFromEndTwoPointer(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        slow = fast = dummyNode

        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummyNode.next

    def createList(self, nums: List) -> Optional[ListNode]:
        curr = None
        for num in nums:
            if not curr:
                curr = ListNode(num)
            else:
                curr.next = ListNode(num)
        
        return curr
    
    def testResult(self, actual: Optional[ListNode], expected: Optional[ListNode]) -> bool:
        actualHead = actual
        expectedHead = expected
        while actualHead:
            if actualHead.val != expectedHead.val:
                return False

            actualHead = actualHead.next
            expectedHead = expectedHead.next
        
        if expectedHead != None or actualHead != None:
            return False
        
        return True

# Tests
# sol = Solution()
# Testcase 1: 
# nums = [1,2,3,4,5]
# n = 2
# expected = [1, 2, 3, 5]

# Testcase 2: 
# nums = [1,2]
# n = 2
# expected = [2]

# Testcase 3: 
# nums = [1,2]
# n = 1
# expected = [1]

# Testcase 4: 
# nums = [1]
# n = 1
# expected = []
