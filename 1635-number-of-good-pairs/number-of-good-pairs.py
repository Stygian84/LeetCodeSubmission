class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dc = defaultdict(int)

        n = len(nums)
        count=0
        for i in range(n):
            if nums[i] in dc:
                count+=dc[nums[i]]
            dc[nums[i]]+=1
        return count
        '''dc={}
        for item in nums:
            if item not in dc:
                dc[item]=1
            else:
                dc[item]+=1
        count=0
        for keys, values in dc.items():
            if values>1:
                count+=math.comb(values,2)
        return count'''
            
        