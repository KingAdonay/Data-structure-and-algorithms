from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # preprocess to find the sum for each window of k
        k_sums = [sum(nums[:k])]
        for i in range(k, n):
            k_sums.append(k_sums[-1] - nums[i - k] + nums[i])

        # use dp to find the max sum of a subarray
        dp = {}
        def find_max(i: int, cnt: int) -> int:
            # len of k_sums = n - k + 1
            if cnt == 3 or i > n - k:
                return 0
            if (i, cnt) in dp:
                return dp[(i,cnt)]
            
            # We have two options at this point
            # Option 1: we can either use the subarray starting from i to i + k - 1 inclusive or
            # Option 2: skip the ith value and start from the next index
            # and then we can take the max of the two options as our max sum
            include = k_sums[i] + find_max(i+k, cnt + 1)
            skip = find_max(i+1, cnt)
            dp[(i, cnt)] = max(include, skip)

            return dp[(i, cnt)]
        
        # find the indices to include by finding the max sum for each i in order (lexicographical order)
        def find_indices():
            i = 0
            indices = []
            while i <= n - k and len(indices) < 3:
                # find max sum for the two possibilities (include or skip)
                # and only use the index if include is greater than skip
                include = k_sums[i] + find_max(i + k, len(indices) + 1)
                skip = find_max(i, len(indices))
                if (include >= skip):
                    indices.append(i)
                    i += k
                else:
                    i += 1
            
            return indices
        
        return find_indices()

# Tests
sol = Solution()
# Testcase 1: [1,2,1,2,6,7,5,1]
print(sol.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2) == [0,3,5])
# Testcase 1: [1,2,1,2,1,2,1,2,1]
print(sol.maxSumOfThreeSubarrays([1,2,1,2,1,2,1,2,1], 2) == [0,2,4])