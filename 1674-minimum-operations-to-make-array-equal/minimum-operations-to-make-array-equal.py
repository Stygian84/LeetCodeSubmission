class Solution:
    def minOperations(self, n: int) -> int:
        # 1 3 5 | 3 2
        # 1 3 5 7 | 4 4
        # 1 3 5 7 9 | 5 6
        # 1 3 5 7 9 11 | 6 9

        res = 0
        for i in range(n//2):
            res += abs((2*i)+1 - n)
        
        return res
    
