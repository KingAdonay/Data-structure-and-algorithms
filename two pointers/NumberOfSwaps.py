'''
    Binary numbers, number of swaps to make all 1's or 0's together
'''

def minSwaps(data):
    n = len(data)
    count_ones = data.count('1')
    count_zeros = n - count_ones

    # Count swaps needed to group all 1's together
    swaps_for_ones = 0
    for i in range(count_ones):
        if data[i] == '0':
            swaps_for_ones += 1

    # Count swaps needed to group all 0's together
    swaps_for_zeros = 0
    for i in range(count_zeros):
        if data[i] == '1':
            swaps_for_zeros += 1

    return min(swaps_for_ones, swaps_for_zeros)

# Test cases
print(minSwaps("1101001"))  # Output: 2
print(minSwaps("10001"))    # Output: 1
print(minSwaps("111000"))   # Output: 0 
print(minSwaps("0101"))   # Output: 1