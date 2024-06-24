class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count={}
        for i in range(1,k+1):
            count[i]=0
        res=0
        while nums:
            num=nums.pop()
            if num in count:
                count[num]+=1
            res+=1
            if all(val>0 for val in count.values()):
                break
        return res