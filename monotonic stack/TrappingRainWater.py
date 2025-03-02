from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        container_count = 0

        for i, h in enumerate(height):
            while stack and stack[-1][0] < h:
                popped_value= stack.pop()
                if stack and stack[-1][0] > popped_value[0]:
                    container_height = min(h, stack[-1][0]) - popped_value[0]
                    base = i - stack[-1][1] - 1
                    area = container_height * base
                    if area > 0:
                        container_count += area
            
            stack.append((h, i))
        return container_count
    
# Tests
sol = Solution()
# Testcase 1: [5,2,1,2,1,5] expected: 14
print(sol.trap([5,2,1,2,1,5]) == 14)
# Testcase 2: [4,2,0,3,2,5] expected: 9
print(sol.trap([4,2,0,3,2,5]) == 9)
# Testcase 3: [0,1,0,2,1,0,1,3,2,1,2,1] expected: 6
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)