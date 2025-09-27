from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        dp_left = [0] * n
        dp_right = [0] * n

        ans = []

        for i in range(1, n):
            if security[i - 1] >= security[i]:
                dp_left[i] = dp_left[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                dp_right[i] = dp_right[i + 1] + 1

        for i in range(n):
            if dp_left[i] >= time and dp_right[i] >= time:
                ans.append(i)
        
        return ans

# Tests
sol = Solution()
# Testcase 1:
print(sol.goodDaysToRobBank([5,3,3,3,5,6,2], 2) == [2,3])
# Testcase 2:
print(sol.goodDaysToRobBank([1,1,1,1,1], 0) == [0,1,2,3,4])
# Testcase 3:
print(sol.goodDaysToRobBank([1,2,3,4,5,6], 2) == [])
# Testcase 4:
print(sol.goodDaysToRobBank([1], 5) == [])