from typing import List, Optional
import heapq

'''
    23. Merge k Sorted Lists
    
    Intuition:
    To merge k sorted linked lists into one sorted linked list, we need to find the minimum element among all the heads of the lists
    and append it to the merged list repeatedly until all the lists are exhauseted.
    
    Approach:
    1. Use a dummy head for the merged linked list to simplify the appending process.
    2. Use a min-heap (priority queue) to efficiently get the minimum element among the heads of the k lists.
    3. Initialize the heap with the heads of all non-empty lists.
    4. While the heap is not empty:
       - Pop the smallest element from the heap.
       - Append it to the merged list.
       - If the popped element has a next node, push that next node onto the heap.
    
    Time complexity:
    - O(N log k), where N is the total number of nodes across all lists and k is the number of lists.
    
    Space complexity:
    - O(k) for the heap storing the heads of the k lists.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        heap = []
        heapq.heapify(heap)

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        while heap:
            val, i = heapq.heappop(heap)
            min_node = lists[i]
            if min_node:
                cur.next = min_node
                lists[i] = lists[i].next
                cur = cur.next
                cur.next = None
                if lists[i]:
                    heapq.heappush(heap, (lists[i].val, i))
        
        return head.next

# Testcases:
if __name__ == "__main__":
    sol = Solution()

    # Helper function to create linked list from list
    def create_linked_list(arr):
        head = ListNode()
        cur = head
        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next
        return head.next

    # Helper function to print linked list
    def check_merged_list(node, expected):
        vals = []
        while node:
            vals.append(node.val)
            node = node.next
        print(vals)
        assert vals == expected
        

    lists = [
        create_linked_list([1,4,5]),
        create_linked_list([1,3,4]),
        create_linked_list([2,6])
    ]
    merged = sol.mergeKLists(lists)
    check_merged_list(merged, [1,1,2,3,4,4,5,6])  # Expected output: [1,1,2,3,4,4,5,6]

    lists = []
    merged = sol.mergeKLists(lists)
    check_merged_list(merged, [])  # Expected output: []

    lists = [None]
    merged = sol.mergeKLists(lists)
    check_merged_list(merged, [])  # Expected output: []