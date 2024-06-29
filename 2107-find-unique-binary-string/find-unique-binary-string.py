class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        res=[]
        for item in nums:
            res.append(int(item,2))

        k=len(nums[0])
        res.sort()
        for i in range(len(res)):
            if res[i]!=i:
                return bin(i)[2:].zfill(k)
        return bin(len(res))[2:].zfill(k)