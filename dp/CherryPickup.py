
from typing import List

'''
    741. Cherry Pickup
    
    Intuition:
    Since we are moving down and right to get to the bottom right corner, we can take the same route back to the top left corner by moving up and left.
    This means rather than going from top left to bottom left and going back, we can just assume that it is two people starting at the same time picking cherries and 
    once a cherry is picked by one person, it cannot be picked by the other person. This is because the greedy approach of picking the maximum cherries
    when going one way and back does not work, we have to do it simultaneously to get the optimal solution.
    
    Approach:
    We can use a recursive approach with memoization to solve this problem.
    1. Define a helper function that takes in the current possitions of the two people (r1, c1) and (r2, c2).
    2. If either of the people goes out of bounds or hits a thorn, return negative infinity to indicate an invalid path.
    3. If person one is at the bottom right corner, return the value of that cell.
    4. Calculate the value of the current cells for both people, if they are on the same cell, only add the value once.
    5. Recursively call the helper function for all possible moves (down, right) for both people and take the maximum of those values.
    6. Store the result in the memoization dictionary and return it.
    7. Finally, call the helper function with the initial positions of both people and return the maximum of the result and 0 (in case all paths are invalid).
    
    Complexity Analysis:
    Time Complexity: O(n^4) in the worst case, since we are exploring all possible positions for both people.
    Space Complexity: O(n^4) in the worst case, since we are storing the results for all possible positions of both people in the memoization dictionary.

'''
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = {}
        def helper(r1, c1, r2, c2) -> int:
            if r1 == n or c1 == n or r2 == n or c2 == n:
                return float('-inf')
            
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            if (r1, c1, r2, c2) in memo:
                return memo[(r1, c1, r2, c2)]

            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            
            val = grid[r1][c1]
            if r1 != r2 or c1 != c2:
                val += grid[r2][c2]
            
            next_max_value = max(
                helper(r1 + 1, c1, r2 + 1, c2), # both down
                helper(r1, c1 + 1, r2, c2 + 1), # both right
                helper(r1 + 1, c1, r2, c2 + 1), # down, right
                helper(r1, c1 + 1, r2+1, c2) # right, down
            )

            memo[(r1, c1, r2, c2)] = val + next_max_value

            return memo[(r1, c1, r2, c2)]
            
        ans = helper(0, 0, 0, 0)
        
        return max(ans, 0)
    
# Testcases:
s = Solution()
print(s.cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]) == 5) # 5
print(s.cherryPickup([[1,1,-1],[1,-1,1],[-1,1,1]]) == 0) # 0
print(s.cherryPickup([[1,1,1,1,-1,-1,-1,1,0,0],[1,0,0,0,1,0,0,0,1,0],[0,0,1,1,1,1,0,1,1,1],[1,1,0,1,1,1,0,-1,1,1],[0,0,0,0,1,-1,0,0,1,-1],[1,0,1,1,1,0,0,-1,1,0],[1,1,0,1,0,0,1,0,1,-1],[1,-1,0,1,0,0,0,1,-1,1],[1,0,-1,0,-1,0,0,1,0,0],[0,0,-1,0,1,0,1,0,0,1]]) == 22) # 22
print(s.cherryPickup([[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]) == 15) # 15
