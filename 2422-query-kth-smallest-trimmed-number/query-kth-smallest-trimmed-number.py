class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        
        res = []
        nums2= []
        for i in range(len(nums)):
            nums2.append((nums[i],i))

        for a,b in queries:
            temp = sorted(nums2,key = lambda x:int(x[0][-b:]))
            #print(temp)
            res.append(temp[a-1][-1])
        
        return res