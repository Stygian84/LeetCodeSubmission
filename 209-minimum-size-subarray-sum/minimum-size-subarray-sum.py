class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        
        i=0
        total=0
        min_length=math.inf

        for j in range(n):
            total+=nums[j]

            while total>=target:
                if j-i+1<min_length:
                    min_length=j-i+1
                total-=nums[i]
                i+=1

        if min_length==math.inf:
            return 0
        return min_length