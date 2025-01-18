import heapq
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sett = set(nums)
        if len(sett) < 3:
            return max(nums)
        
        heap = [float('-inf')] * 3
        heapq.heapify(heap)

        for num in nums: 
            if num in heap:
                continue
            
            heapq.heappushpop(heap, num)
        
        return heap[0]
        

solution = Solution()
# Tests
# Testcase 1: [2,2,3,1] 3rd max = 1
maxx = solution.thirdMax([2,2,3,1])
print(maxx == 1)
# Testcase 1: [1,2] 3rd max = 2
maxx = solution.thirdMax([1,2])
print(maxx == 2)
# Testcase 1: [3,2,1] 3rd max = 1
maxx = solution.thirdMax([3,2,1])
print(maxx == 1)