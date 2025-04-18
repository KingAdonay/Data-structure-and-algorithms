from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        player1, player2 = self.recursive(nums, 0, len(nums) - 1, {}, True)

        return player1 >= player2
    
    def recursive(self, nums: List[int], start: int, end: int, storage: dict,  isPlayerOne: bool) -> List[int]:
        tupl = (start, end, isPlayerOne)
        if tupl in storage:
            return storage[tupl]

        idx = int(isPlayerOne) - 1
        if start == end:
            arr = [0, 0]
            arr[idx] = nums[start]
            storage[tupl] = arr
            return arr
        
        res1 = self.recursive(nums, start + 1, end, storage, not isPlayerOne).copy()
        res2 = self.recursive(nums, start, end - 1, storage, not isPlayerOne).copy()

        res1[idx] += nums[start]
        res2[idx] += nums[end]

        ans = res1 if res1[idx] > res2[idx] else res2
        
        storage[tupl] = ans
        return ans
            

# Tests
sol = Solution()
# Testcase 1: [1,2,3,4,999,3]
print(True == sol.predictTheWinner([1,2,3,4,999,3]))
# Testcase 2: [1,2,3,4,5]
print(True == sol.predictTheWinner([1,2,3,4,5]))
# Testcase 3: [1,5,2]
print(False == sol.predictTheWinner([1,5,2]))
# Testcase 4: [1,5,233,7]
print(True == sol.predictTheWinner([1,5,233,7]))
# Testcase 5: [1]
print(True == sol.predictTheWinner([1]))
# Testcase 6: [1,5]
print(True == sol.predictTheWinner([1,5]))