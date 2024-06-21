class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dc={}
        for num in nums:
            if num%2==0:
                dc[num]=dc.get(num,0)+1
        if not dc:
            return -1
        max_values=0
        res=-1
        for key,values in dc.items():
            if values>max_values:
                res=key
                max_values=values
            elif values==max_values:
                if key<res:
                    res=key
        return res