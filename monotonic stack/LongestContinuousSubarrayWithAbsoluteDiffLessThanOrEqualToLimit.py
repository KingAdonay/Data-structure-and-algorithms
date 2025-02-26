from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        max_length = 0
        max_queue = deque([]) # decreasing monotonic queue
        min_queue = deque([]) # increasing monotonic queue

        i = -1 # left
        j = 0 # right

        while j < n:
            while max_queue and nums[max_queue[-1]] < nums[j]:
                max_queue.pop()
            max_queue.append(j)

            while min_queue and nums[min_queue[-1]] > nums[j]:
                min_queue.pop()
            min_queue.append(j)

            while abs(nums[max_queue[0]] - nums[min_queue[0]]) > limit:
                i += 1

                if min_queue and min_queue[0] <= i:
                    min_queue.popleft()
                
                if max_queue and max_queue[0] <= i:
                    max_queue.popleft()
 
            max_length = max(max_length, j - i)
            j += 1
        
        return max_length
    

# Tests
sol = Solution()
# Testcase 1: nums = [8,2,4,7], limit = 4
ans = sol.longestSubarray([8,2,4,7], 4)
print(ans == 2)
# Testcase 2: nums = [10,1,2,4,7,2], limit = 5
ans = sol.longestSubarray([10,1,2,4,7,2], 5)
print(ans == 4)
# Testcase 3: nums = [4,2,2,2,4,4,2,2], limit = 0
ans = sol.longestSubarray([4,2,2,2,4,4,2,2], 0)
print(ans == 3)
# Testcase 4: nums = [1,5,6,7,8,10,6,5,6], limit = 4
ans = sol.longestSubarray([1,5,6,7,8,10,6,5,6], 4)
print(ans == 5)
