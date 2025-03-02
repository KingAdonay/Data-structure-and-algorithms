# -> Used a monotonically increasing stack to find the next smallest value (this 
# will be the right pointer - end of the rectangle)
# -> Remember the position of the value in the stack to use as the left pointer 
# (start of the rectangle)
# -> Everytime we find a value less than our top of the stack value, we would pop the top from the stack and calculate the area for that popped height using the left and right pointers 
# -> a = height * (r - l)
# -> If found the same consecutive values, keep only the one with the smallest position
# -> If there are values left in the stack, that means those bars can create a rectangle 
# that could extend up to the end of the chart so we will use the length of the data as the right pointer and calculate the area
# -> Everytime we calculate an area, we should compare it with the max_area and keep the maximum out of the two compared areas.

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] # stack of tuple (height, left)
        
        max_area = 0
        for idx, height in enumerate(heights):
            left = idx
            while stack and stack[-1][0] > height:
                h, position_in_stack = stack.pop()
                left = position_in_stack
                area = h * (idx - left)
                max_area = max(max_area, area)

            if stack and stack[-1][0] == height:
                continue # only keep the height with the smalles left pointer for the same height
            
            stack.append((heights[idx], left))
            
        while stack:
            h, left = stack.pop()
            area = h * (n - left)
            max_area = max(max_area, area)

        return max_area  

# Tests
sol = Solution()
# Tescase 1: [2,1,5,6,2,3] expected = 10
print(sol.largestRectangleArea([2,1,5,6,2,3]) == 10)
# Tescase 2: [2,4] expected = 4
print(sol.largestRectangleArea([2,4]) == 4)