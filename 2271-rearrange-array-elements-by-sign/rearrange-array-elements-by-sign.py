class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        for item in nums:
            if item<0:
                negative+=[item]
            else:
                positive+=[item]
        res=[]
        for idx in range(len(positive)):
            res.append(positive[idx])
            res.append(negative[idx])
        return res