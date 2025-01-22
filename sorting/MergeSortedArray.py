class Solution:
    def partition(self, nums, left, right):
        pivot = nums[right]
        i = left - 1
        j = left
        while j < right:
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            
            j += 1
        
        i += 1
        nums[i], nums[right] = nums[right], nums[i]

        return i
    
    def quickSort(self, nums, left, right):
        if left >= right: 
            return
        
        pi = self.partition(nums, left, right)

        self.quickSort(nums, left, pi - 1)
        self.quickSort(nums, pi + 1, right)
    
    def merge(self, nums1, m, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        while i < m + n:
            nums1[i] = nums2[i - m]
            i += 1
        
        self.quickSort(nums1, 0, m + n - 1)

# Tests
# Testcase 1:
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()

solution.merge(nums1, m, nums2, n)
print(nums1 == [1,2,2,3,5,6])