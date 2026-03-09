import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [-1 * num for num in nums]
        heapq.heapify(heap)

        while k > 1 and heap:
            heapq.heappop(heap)
            k -= 1

        return -1 * heap[0]