def get_max_diversity(nums):
    sett = set()
    duplicates = set()
    
    n = len(nums)
    for i in range(n):
        value = abs(nums[i])
        if value not in sett:
            sett.add(value)
        elif value != 0:
            duplicates.add(value)
    
    unique_variations = len(sett) + len(duplicates)
    
    return unique_variations
    
    
if __name__ == "__main__":
    num_of_tests = int(input())
    nums = []
    i = 0
    while i < num_of_tests:
        n = input()
        arr = list(map(int, input().rstrip().split()))
        nums.append(arr)
        
        i += 1
        
    i = 0
    while i < num_of_tests:
        max_variations = get_max_diversity(nums[i])
        print(max_variations)
        i += 1

# Test inputs
# 3
# 4
# 1 1 2 2
# 3
# 1 2 3
# 2
# 0 0

# output
# 4
# 3
# 1
