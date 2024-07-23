class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dc=Counter(nums)
        ls = sorted(dc.items(), key = lambda x : (x[1],-x[0]))
        
        res = []

        for item in ls:
            res+=[item[0]]*item[1]


        return res