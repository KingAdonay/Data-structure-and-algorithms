from typing import List


def partition( nums, left, right) -> int:
        pivot = nums[right]
        i = left - 1
        j = left
        while j < right:
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        
        nums[i + 1], nums[right] = nums[right], nums[i + 1]

        return i + 1


def quickSort(nums:List[int], left, right):
    if left >= right:
        return
    
    pi = partition(nums, left, right)

    quickSort(nums, left, pi - 1)
    quickSort(nums, pi + 1, right)
