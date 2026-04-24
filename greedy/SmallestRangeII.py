class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(n - 1):
            a, b = nums[i], nums[i+1]
            maxx = max(nums[-1] - k, a + k)
            minn = min(nums[0] + k, b - k)
            ans = min(ans, maxx - minn)
            
        return ans
        
'''
Testcases
[0,10], 2 -> 6
[1,3,6], 3 -> 3
'''