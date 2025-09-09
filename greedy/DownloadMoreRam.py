from typing import List
from functools import cmp_to_key

def comparator_fun (a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] == b[0]:
        if a[1] < b[1]:
            return -1
    
    return 1

comparator_key = cmp_to_key(comparator_fun)

def calculate_max_ram(k: int, n: int, storage_needed: List[int], storage_added: List[int]) -> None:
    storages = list(zip(storage_needed, storage_added))
    storages.sort(key=comparator_key)
    
    curr_sg = k
    for storage in storages:
        sg_needed, sg_added = storage
        
        if curr_sg >= sg_needed:
            curr_sg += sg_added
        else:
            break
    
    print(curr_sg)

if __name__ == '__main__':
    n_of_tests = int(input())
    tests = []
    for i in range(n_of_tests):
        n, k = map(int, input().split(' '))
        storage_needed = map(lambda x: int(x), input().split(' '))
        storage_to_add = map(int, input().split(' '))
        
        tests.append((k, n, storage_needed, storage_to_add))
    
    for test in tests:
        k, n, sn, sa = test
        calculate_max_ram(k, n, sn, sa)

# Testcase example
# Input:
# 1
# 3 10
# 20 30 10
# 9 100 10
# Output: 29