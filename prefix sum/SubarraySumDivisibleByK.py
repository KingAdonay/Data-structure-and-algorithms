class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        remainders = defaultdict(int)
        remainders[0] = 1
        ans = 0
        for num in nums:
            prefix += num
            r = prefix % k
            ans += remainders[r]
            remainders[r] += 1

        return ans
            