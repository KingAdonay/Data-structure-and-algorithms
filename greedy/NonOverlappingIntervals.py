'''
435. Non-overlapping intervals

Use greedy approach.

Sort the intervals with the end time, ascendingly, and remove the next overlapping interval found, which would increase the possibility of the longest interval that might cover other intervals.

Time complexity: O(nlogn)
Space complexity: O(logn)
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        ans = 0
        last_end = float('-inf')
        
        for a, b in intervals:
            if last_end > a:
                ans += 1
            else:
                last_end = b
        
        return ans
        

'''
Testcases:

[[1,2],[2,3],[3,4],[1,3]] -> 1
[[1,2],[1,2],[1,2]] -> 2
'''

