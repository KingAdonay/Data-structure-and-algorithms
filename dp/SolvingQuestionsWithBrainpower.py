from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = {}

        def helper(i):
            if i >= len(questions):
                return 0
            if i in cache:
                return cache[i]

            points, brainpower = questions[i]
            # answer question
            ans_res = points + helper(i + brainpower + 1)
            # skip question
            skip_res = helper(i+1)

            cache[i] = max(ans_res, skip_res)
            return cache[i]
        
        return helper(0)
    
    def mostPointsBottomUp(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            solve = points + (dp[i + brainpower + 1] if i + brainpower + 1 <= n else 0)
            skip = dp[i + 1]
            dp[i] = max(solve, skip)

        return dp[0]
    
# Tests
sol = Solution()
# Testcase 1
questions = [[3,2],[4,3],[4,4],[2,5]]
print(sol.mostPoints(questions) == 5)
# Testcase 2
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
print(sol.mostPoints(questions) == 7)
# Testcase 3
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
print(sol.mostPointsBottomUp(questions) == 7)
# Testcase 4
questions = [[3,2],[4,3],[4,4],[2,5]]
print(sol.mostPointsBottomUp(questions) == 5)