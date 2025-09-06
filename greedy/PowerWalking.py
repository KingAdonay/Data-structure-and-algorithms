from typing import List

def power_walking(n:int, power_ups:List[str]) -> None:
    sett = set(power_ups)
    distinct = len(sett)
    
    for i in range(1, n+1):
        if i <= distinct:
            print(distinct)
        else:
            print(distinct + (i - distinct))

if __name__ == '__main__':
    number_of_testcases = int(input())
    testcases = []
    for i in range(number_of_testcases):
        n = int(input())
        power_ups = input().split(' ')
        testcases.append({'n': n, 'power_ups': power_ups})
    
    for testcase in testcases:
        power_walking(testcase['n'], testcase['power_ups'])