
def summ (nums, start, end):
    return sum(nums[start:end+1])

def can_paint(seq):
    seq.sort()

    n = len(seq)
    left, right = 0, n-1
    while left < right:
        is_sum_greater = summ(seq, right, n-1) > summ(seq, 0, left)
        is_count_less = n - right < left + 1
        
        while not is_sum_greater and right - 1 > left:
            right -= 1
            is_sum_greater = summ(seq, right, n-1) > summ(seq, 0, left)
            is_count_less = n - right < left + 1
        
        if is_sum_greater and is_count_less:
            print('YES')
            return
        
        left += 1
    
    print('NO')

if __name__ == "__main__":
    n_of_tests = int(input())
    tests = []
    for i in range(n_of_tests):
        n = int(input())
        seq = list(map(int, input().split(' ')))
        tests.append(seq)
    
    for test in tests:
        can_paint(test)


# Testcasaes
'''
1
10
14 15 15 15 19 16 14 18 16 10

Output: YES
'''

'''
1
3
1 2 3

Output: NO
'''