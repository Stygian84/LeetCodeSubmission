class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        idx = defaultdict(list) #value:idx

        for i in range(len(nums)):
            idx[nums[i]].append(i)
        
        for a,b in operations:
            idx[b] = idx[a]
            idx[a] = []

        res = [0]*len(nums)

        for k,v in idx.items():
            for i in v:
                res[i]=k
        
        return res



        '''dc = {}
        n = len(nums)

        for i in range(n):
            dc[nums[i]] = i
        print(dc)        
        dc2 = {}
        for old,new in operations:
            if old in dc:
                dc2[new]=dc[old]
            else:
                dc2[new]=dc2[old]
        res = nums[:]

        for k,v in dc2.items():
            res[v]=k
        
        return res'''
