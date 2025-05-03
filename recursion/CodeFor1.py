def check_count_of_ones(num_input, l, r):
    def helper(num):
        if num <= 1:
            return [num]
        
        
        num_div_res = num // 2
        num_mod = num % 2

        res = helper(num_div_res)
        
        return res + [num_mod] + res

    
    reduced_list = helper(num_input)
    
    count = 0
    i = l - 1
    while i < r and i < len(reduced_list):
        if reduced_list[i] == 1:
            count += 1
        
        i += 1
        
    return count
    
    
if __name__ == "__main__":
    
    values = input().split()
    num = int(values[0])
    l = int(values[1])
    r = int(values[2])
    res = check_count_of_ones(num, l, r)
    print(res)

# Tests
# Testcase 1: 7 2 5, res = 4
# Testcase 2: 10 3 10 res = 5
# Testcase 3: 56 18 40 10 res = 20
# Testcase 4: 203 40 124 10 res = 20
# Testcase 5: 903316762502 354723010040 354723105411 (MEMORY_LIMIT_EXCEEDED) 
