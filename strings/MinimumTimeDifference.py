from typing import List

'''
    539. Minimum Time Difference
    
    Convert each time string to minutes and sort them. Then find the minimum difference between consecutive time points, including
    the circular difference between the last and first time points.
    
    Time Complexity: O(N log N) due to sorting the time points.
    Space Complexity: O(N) for storing the time points in minutes.

'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            hour_st, min_st = time.split(':')
            m = int(hour_st) * 60 + int(min_st)
            minutes.append(m)
        
        minutes.sort()
        n = len(minutes)
        
        min_diff = (1440 - minutes[n - 1]) + minutes[0] # Circular difference between last and first time point

        for i in range(1, n):
            diff = minutes[i] - minutes[i-1]
            min_diff = min(min_diff, diff)
        
        return min_diff

# Testcases
sol = Solution()
print(sol.findMinDifference(["23:59","00:00"]) == 1)  # Output: 1
print(sol.findMinDifference(["00:00","23:59","12:30"]) == 1)  # Output: 1
print(sol.findMinDifference(["01:01","02:01","03:00"]) == 59)  # Output: 59
print(sol.findMinDifference(["12:12","00:13"]) == 719)  # Output: 719
print(sol.findMinDifference(["05:31","22:08","00:35"]) == 147)  # Output: 147