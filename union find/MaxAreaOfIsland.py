from typing import List, Tuple

'''
695. Max Area of Island

Use union find to group the land cells (1s) together by tracking parents in a 2D array. 
Each cell points to its parent cell, and the weight is stored in the parent cell as a tuple (weight, -1), negative weight
for head nodes. During union operstions, we update the weights accordingly. 

Finally, we return the maximum weight (abs(min_weight) since we are using negative weight) found among the head nodes.

Time complexity: O(m * n), where m and n are the dimensions of the grid.
Space complexity: O(m * n) for the parents array.
'''
class Solution:
    def find(self, i: int, j: int) -> Tuple[int, int, int]:
            parent_i, parent_j = self.parents[i][j]
            if parent_i < 0:
                return i, j, parent_i
            
            return self.find(parent_i, parent_j)
    
    def union(self, i1: int, j1: int, i2: int, j2: int) -> None:
            parent_1_i, parent_1_j, weight1 = self.find(i1, j1)
            parent_2_i, parent_2_j, weight2 = self.find(i2, j2)

            if parent_1_i == parent_2_i and parent_1_j == parent_2_j:
                return
            
            new_weight = weight1 + weight2
            if weight1 <= weight2:
                self.parents[i2][j2] = (parent_1_i, parent_1_j)
                self.parents[parent_2_i][parent_2_j] = (parent_1_i, parent_1_j)
                self.parents[parent_1_i][parent_1_j] = (new_weight, -1)
            else:
                self.parents[i1][j1] = (parent_2_i, parent_2_j)
                self.parents[parent_1_i][parent_1_j] = (parent_2_i, parent_2_j)
                self.parents[parent_2_i][parent_2_j] = (new_weight, -1)
            
            self.min_weight = min(self.min_weight, new_weight)
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        self.parents = [[(-1, -1) for i in range(n)].copy() for j in range(m)]
        self.min_weight = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.min_weight = min(self.min_weight, self.parents[i][j][0])
                    if i - 1 >= 0 and grid[i-1][j] == 1:
                        self.union(i, j, i-1, j)
                    if j - 1 >= 0 and grid[i][j-1] == 1:
                        self.union(i, j, i, j-1)

    
        return abs(self.min_weight)

# Testcases:
s = Solution()
print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6) # 6
print(s.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0) # 0
print(s.maxAreaOfIsland([[0,0],[0,1]]) == 1) # 1