class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        
        maximum = 0
        res = math.inf
        
        for d in divisors:
            count = 0
            for num in nums:
                if num%d==0:
                    count+=1

            if count > maximum:
                maximum=count
                res=d
            elif count == maximum:
                res = min(res,d)  

        return res