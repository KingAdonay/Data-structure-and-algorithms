from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        cache = {}

        def find_next_index(i):
            l, r, next_index = i + 1, n-1, n
            while l <= r:
                mid = (r + l) // 2
                
                if events[mid][0] > events[i][1]:
                    next_index = mid
                    r = mid - 1
                else:
                    l = mid + 1

            return next_index

        def helper(i, k):
            if i >= n or k == 2:
                return 0

            key = (i,k)
            if key in cache:
                return cache[key]

            next_index = find_next_index(i)

            choose = events[i][2] + helper(next_index, k + 1)
            skip = helper(i + 1, k)

            cache[key] = max(choose, skip)
            return cache[key]

        events.sort(key=lambda x:x[0])
        return helper(0,0)
        
# Tests
sol = Solution()
# Testcase 1: [[1,3,2],[4,5,2],[2,4,3]]
print(sol.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]) == 4)
# Testcase 2: [[1,3,2],[4,5,2],[1,5,5]]
print(sol.maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]) == 5)