from typing import List

'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Solution: Use DP to build heights array for each row, then use monotonic stack to find the largest rectangle in histogram for each row.
'''
class Solution:
    def find_max_rectangle(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                max_area = max(max_area, h * (i - idx))
                start = idx
            
            stack.append((start, height))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * cols

        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    dp[j] = dp[j] + int(matrix[i][j])
                else:
                    dp[j] = 0
                    
            max_area = max(self.find_max_rectangle(dp), max_area)
        
        return max_area

# Tests
sol = Solution()
# Testcase 1
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
print(sol.maximalRectangle(matrix) == 6)
# Testcase 2
matrix = [["0"]]
print(sol.maximalRectangle(matrix) == 0)
# Testcase 3
matrix = [["1"]]
print(sol.maximalRectangle(matrix) == 1)
# Testcase 4
matrix = [["0","0"]]
print(sol.maximalRectangle(matrix) == 0)
# Testcase 5
matrix = [["1","1"]]
print(sol.maximalRectangle(matrix) == 2)
# Testcase 6
matrix = [["1","0"]]
print(sol.maximalRectangle(matrix) == 1)