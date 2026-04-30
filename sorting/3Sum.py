class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:    
        nums.sort()
    
        ans = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                summ = num + nums[left] + nums[right]
                if summ == 0:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif summ > 0:
                    right -= 1
                else:
                    left += 1
            
        return ans
                    
        
        
                
'''
[-1,0,1,2,-1,-4] -> [[-1,-1,2], [-1,0,1]]
'''