class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        res = math.inf
        for num in nums:
            total = 0
            for digit in str(num):
                total+=int(digit)
            if total<res:
                res=total
        return res