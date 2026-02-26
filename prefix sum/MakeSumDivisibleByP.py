from typing import List

'''
    1590. Make Sum Divisible by P
    
    To find the minimum length of a subarray that can be removed to make the sum divisible by p, we can iterate through each element
    and use each element as a start and iterate through the rest of the elements subtracting from the total sum until we get a remainder of 0 when we divide the sum by p.
    However, this approach is inefficient for a large array.
    A more efficient approach is to use a prefix sum and a hash map to track the prefix sums mod p.
    We can track the mod value of the prefix sum with the index in a hash map.
    
    The steps of the algorithm are as follows:
    1. Calculate the total sum of the array and find the target mod value by taking the total sum mod p.
    2. If the target mod value is 0, it means the sum is already divisible by p, so we can return 0.
    3. Initialize a hash map to track the prefix sums mod p, starting with the value 0 at index -1.
    4. Iterate through the array and calculate the prefix sum mod p at each index.
       a. For each prefix sum mod p, calculate the needed mod value to reach the target mod value.
       b. If the needed mod value is found in the hash map, it means we can remove the subarray between the index of the needed mod value and the current index to achieve a sum that is divisible by p. Update the minimum length of the subarray to be removed.
       c. Update the hash map with the current prefix sum mod p and its index.
    5. Finally, return the minimum length of the subarray to be removed, or -1 if no such subarray exists.
    
    Time Complexity: O(n) due to the single pass through the array.
    Space Complexity: O(n) for the hash map to store prefix sums mod p.
'''

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        summ = sum(nums)
        n = len(nums)
        min_len = n

        target = summ % p
        if target == 0:
            return 0
        # Use a dict to track prefix sum mod p
        prefix = {0: -1}
        cur_sum = 0
        for i in range(n):
            cur_sum = (cur_sum + nums[i]) % p
            needed = (cur_sum - target + p) % p
            if needed in prefix:
                min_len = min(min_len, i - prefix[needed])
            
            prefix[cur_sum] = i
        
        return min_len if min_len != n else -1
    
# Testcases:
s = Solution()
print(s.minSubarray([3,1,4,2], 6) == 1)
print(s.minSubarray([6,3,5,2], 9) == 2)
print(s.minSubarray([1,2,3], 3) == 0)
print(s.minSubarray([1,2,3], 7) == -1)
print(s.minSubarray([1000000000,1000000000,1000000000], 3) == 0)