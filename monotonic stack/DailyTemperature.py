from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []

        i = n - 1
        while i >= 0:
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            count = 0
            if stack:
                count = stack[-1][1] - i

            stack.append((temperatures[i], i))  
            ans[i] = count
            i -= 1

        return ans
    
# Tests
sol = Solution()
# Testcases 1:
days = sol.dailyTemperatures([73,74,75,71,69,72,76,73])
print(days == [1,1,4,2,1,1,0,0])
# Testcase 2: [30,40,50,60] [1, 1, 1, 0]
