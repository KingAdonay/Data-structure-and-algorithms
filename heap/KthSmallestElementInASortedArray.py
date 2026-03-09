import heapq
from typing import List

'''
    378. Kth Smallest Element in a Sorted Matrix

    - We can use a max heap to keep track of the k smallest elements in the matrix.
    - We iterate through each element in the matrix and add it to the heap, while keeping the size of the heap limited to k.
    - If the heap exceeds size k, we remove the largest element (the root of the max heap).
    - After processing all elements, the root of the max heap will be the k-th smallest element in the matrix.
    
    Time Complexity: O(n^2 log k) - We iterate through all n^2 elements and each insertion/deletion in the heap takes O(log k).
    Space Complexity: O(k) - The heap will contain at most k elements. 
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []

        for i in range(n):
            for j in range(n):
                heapq.heappush(heap, -1 * matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        
        return -1 * heap[0]

# Testcases:
sol = Solution()
print(sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13)
print(sol.kthSmallest([[1,2],[1,3]], 2) == 1)