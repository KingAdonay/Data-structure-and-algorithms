from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        curr = head
        stack = []

        while curr:
            while stack and stack[-1][1] < curr.val:
                idx, val = stack.pop()
                ans[idx] = curr.val
            
            stack.append((len(ans), curr.val))
            ans.append(0)
            curr = curr.next
        
        return ans

# Tests
# Testcase 1: [2,1,5]
# Testcase 2: [2,7,4,3,5]