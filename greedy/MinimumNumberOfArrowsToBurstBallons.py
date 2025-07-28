from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)

        points.sort(key=lambda point:(point[0], point[1]))

        arrow_count = 1
        start = points[0][0]
        end = points[0][1]
        for i in range(n):
            if not (start <= points[i][0] <= end or start <= points[i][1] <= end):
                arrow_count += 1
                end = points[i][1]

            start = max(points[i][0], start)
            end = min(points[i][1], end)
        return arrow_count
    
# Tests
sol = Solution()
# Testcase 1:
print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2)
# Testcase 2:
print(sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4)
# Testcase 3:
print(sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2)
# Testcase 4:
print(sol.findMinArrowShots([[1,2]]) == 1)
# Testcase 5:
print(sol.findMinArrowShots([[2,3],[2,3]]) == 1)
# Testcase 6:
print(sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10]]) == 5)
# Testcase 7:
print(sol.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]) == 2)