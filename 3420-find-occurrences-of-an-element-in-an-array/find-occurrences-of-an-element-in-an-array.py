class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        dc={}
        count=1
        for i in range(len(nums)):
            num = nums[i]
            if num == x:
                dc[count] = i
                count += 1
        
        res = []
        for query in queries:
            res.append( dc.get(query,-1) )
        return res