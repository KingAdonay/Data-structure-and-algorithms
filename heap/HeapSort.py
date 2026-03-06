from typing import List
import heapq

'''

Heap Sort Implementation using Python's heapq module
Intuition:
Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements.
The basic idea is to build a min-heap from the input data and then repeatedly extract the minimum element from the heap and add it to the sorted output list until the heap is empty.

Time complexity: O(n log n) where n is the number of elements in the input list
Space complexity: O(n) for the output list, and O(1) for the in-place heap operations.

'''

class Solution:
    def heapSort(self, arr: List[int]) -> List[int]:
        heapq.heapify(arr)
        n = len(arr)
        
        res = []
        
        while arr:
            res.append(heapq.heappop(arr))
            
        return res


# Testcases:
sol = Solution()
print(sol.heapSort([3,4,5,6,7,2]) == [2,3,4,5,6,7])
print(sol.heapSort([67,596,680,294,916,544,738]) == [67,294,544,596,680,738,916])