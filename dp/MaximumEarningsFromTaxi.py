from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:

        def find_next_valid_idx(i):
            l, r, idx = i + 1, len(rides) - 1, len(rides)
            while l <= r:
                mid = (l + r) // 2
                if rides[mid][0] >= rides[i][1]:
                    idx = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            return idx
        
        def helper(i, storage):
            if i >= len(rides):
                return 0
            if i in storage:
                return storage[i]
            
            start, end, tip = rides[i]
            payment = end - start + tip

            next_valid_idx = find_next_valid_idx(i)

            take_ride = payment + helper(next_valid_idx, storage)
            skip_ride = helper(i + 1, storage)

            storage[i] = max(take_ride, skip_ride)

            return storage[i]
        
        rides.sort(key = lambda x:x[0])

        return helper(0, {})

# Tests
sol = Solution()
# Testcase 1: n = 5, rides = [[2,5,4],[1,5,1]]
print(sol.maxTaxiEarnings(5, [[2,5,4],[1,5,1]]) == 7)
# Testcase 2: n = 20, rides = [[1,6,1],[3,10,2],[10,13,2],[11,12,3],[12,15,2],[13,18,1]]
print(sol.maxTaxiEarnings(20, [[1,6,1],[3,10,2],[10,13,2],[11,12,3],[12,15,2],[13,18,1]]) == 20)