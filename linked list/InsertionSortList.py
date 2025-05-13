# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortListUsingArr(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [None] * 5000
        i = 0
        curr = head
        
        while curr:
            arr[i] = curr
            next_node = curr.next
            
            j = i - 1
            node = None
            while j >= 0:
                node = arr[j]
                if node.val <= curr.val:
                    break
                j -= 1
            
            if j == -1:
                curr.next = arr[0]
            elif node:
                next_of_node = node.next
                node.next = curr
                curr.next = next_of_node
            
            popped_node = arr.pop(i)
            arr.insert(j+1, popped_node)
            arr[i].next = next_node
                
            curr = next_node
            i += 1
            
        return arr[0]
    
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001, head)
        prev, curr = dummy.next, dummy.next.next

        while curr:
            if curr.val >= prev.val:
                prev, curr = curr, curr.next
                continue
            
            smaller_node = dummy
            while smaller_node.next and smaller_node.next.val < curr.val:
                smaller_node = smaller_node.next
            
            prev.next = curr.next
            curr.next = smaller_node.next
            smaller_node.next = curr
            curr = prev.next
        
        return dummy.next

# Tests
# Testcase 1: [4,2,1,3]
# Testcase 2: [-1,5,3,4,0]
# Testcase 3: [4,2]
# Testcase 4: [1,3]
# Testcase 5: [1]