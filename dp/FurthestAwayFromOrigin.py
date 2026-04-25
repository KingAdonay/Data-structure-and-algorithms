class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        mapp = {'L': -1, 'R': 1}
        
        @cache
        def helper(i, summ):
            if i == len(moves):
                return summ
            
            if moves[i] == '_':
                left = helper(i + 1, summ - 1)
                right = helper(i + 1, summ + 1)
                if abs(left) > abs(right):
                    return left
                else:
                    return right
            
            return helper(i + 1, summ + mapp[moves[i]])
        
        return abs(helper(0, 0))
        
'''
"L_RL__R" -> 3
"_R__LL_" -> 5
'''