from typing import List

'''
    739. Daily Temperatures
    Intuition:
    We can use a monotonically decreasing stack to keep track of the temperatures and their indices. 
    For each temperature, we will pop from the stack until we find a temperature that is greater than the current temperature. 
    The difference between the current index and the index of the temperature at the top of the stack will give us the number of days until a warmer temperature.

    Approach:
    1. Initialize an empty stack and an answer list with 0s.
    2. Iterate through the temperatures from right to left.
    3. For each temperature, pop from the stack until we find a temperature that is greater than the current temperature.
    4. If the stack is not empty, calculate the number of days until a warmer temperature and update the answer list.
    5. Push the current temperature and its index onto the stack.
    6. Return the answer list.

    Time complexity: O(n) where n is the number of temperatures
    Space complexity: O(n) for the stack and answer list
'''

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
