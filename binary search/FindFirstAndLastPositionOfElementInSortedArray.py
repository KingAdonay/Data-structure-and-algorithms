class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(num):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        idx1, idx2 = binary_search(target), binary_search(target + 1)

        if not (0 <= idx1 < len(nums)) or nums[idx1] != target:
            return [-1, -1]

        return [idx1, idx2 - 1 if idx2 > idx1 else idx2]
        