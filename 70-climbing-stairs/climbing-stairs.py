class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        result=0
        result_1=1
        result_2=2

        for i in range(2, n):
            result =  result_1+result_2
            result_1,result_2=result_2,result

        return result