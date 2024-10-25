class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        current = 0

        res = []
        for num in nums:
            current<<=1
            if num==1:
                current |= 1
            if current%5==0:
                res.append(True)
            else:
                res.append(False)
        return res