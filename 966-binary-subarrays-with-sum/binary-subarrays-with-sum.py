class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count=defaultdict(int)
        prefix_count[0]=1
        prefix_sum=0

        count=0
        
        for num in nums:
            prefix_sum+=num
            count+=prefix_count.get(prefix_sum-goal,0)
            prefix_count[prefix_sum]+=1
            
        return count