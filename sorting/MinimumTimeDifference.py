from typing import List

class Solution:
    def convert_to_minute(self, time_str: str) -> int:
        time_arr = time_str.split(':')
        hh_in_min = int(time_arr[0]) * 60
    
        return hh_in_min + int(time_arr[1])
        
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)

        min_arr = []
        for time in timePoints:
            min_arr.append(self.convert_to_minute(time))
        
        min_arr.sort()
        minn = ((24 * 60) - min_arr[n - 1]) + min_arr[0]
        
        for i in range(1, n):
            diff = min_arr[i] - min_arr[i - 1]
            minn = min(minn, diff)
        
        return minn

# Tests
sol = Solution()

# Testcase 1: ["02:39","10:26","21:43"]
min_time_diff = sol.findMinDifference(["02:39","10:26","21:43"])
print(min_time_diff == 296)
# Testcase 2: ["00:00","23:59","00:00"]
min_time_diff = sol.findMinDifference(["00:00","23:59","00:00"])
print(min_time_diff == 0)
# Testcase 3: ["23:59","00:00"]
min_time_diff = sol.findMinDifference(["23:59","00:00"])
print(min_time_diff == 1)