from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(n):
            left = max(0, i - 1)

            if ratings[i] > ratings[left]:
                candies[i] = candies[left] + 1
        
        for i in range(n-1, -1, -1):
            right = min(i + 1, n-1)
            if ratings[i] > ratings[right]:
                candies[i] = max(candies[i], candies[right] + 1)
        
        return sum(candies)

# Tests
sol = Solution()
# Testcase 1:
print(sol.candy([1,0,2]) == 5)
# Testcase 2:
print(sol.candy([1,2,2]) == 4)
# Testcase 3:
print(sol.candy([1,3,4,5,2]) == 11)
# Testcase 4:
print(sol.candy([1,2,87,87,87,2,1]) == 13)
# Testcase 5:
print(sol.candy([1,6,10,8,7,3,2]) == 18)
# Testcase 6:
print(sol.candy([6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0]) == 42)