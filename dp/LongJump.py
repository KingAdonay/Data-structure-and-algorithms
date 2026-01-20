'''
    Codeforces problem Long Jump
    
    Use dynamic programming to find the maximum distance that can be covered by jumping through an array.
    For each position, calculate the maximum distance that can be achieved by jumping from that position
    to the position indicated by the value at that position, and add the value at that position.
    
    Time complexity: O(n) where n is the length of the input array
    Space complexity: O(n)
'''

def long_jump(nums):
    dp = [0] * len(nums)
    max_num = 0
    for i in range(len(nums) - 1, -1, -1):
        cur = nums[i]
        landing_position = i + cur
        dp[i] = cur
        if landing_position < len(nums):
            dp[i] += dp[landing_position]
        
        max_num = max(max_num, dp[i])
    
    
    print(max_num)

if __name__ == "__main__":
    n = int(input())
    
    inputs = []
    while n > 0:
        size = input()
        nums_st = input()
        nums = [int(num) for num in nums_st.split(' ')]
        inputs.append(nums)
        n -= 1
    
    for nums in inputs:
        long_jump(nums)
        
# Testcases
# long_jump([7 3 1 2 3])  # Expected output: 7
# long_jump([2 1 4])  # Expected output: 6

# Input example:
# 2
# 5
# 7 3 1 2 3

#  Output:
# 7