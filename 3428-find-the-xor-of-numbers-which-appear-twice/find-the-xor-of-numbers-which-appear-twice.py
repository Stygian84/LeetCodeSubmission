class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dc={}
        for num in nums:
            dc[num]=dc.get(num,0)+1
        res=0

        for key,values in dc.items():
            if values==2:
                res^=key

        return res

