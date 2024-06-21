class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix=[]
        for item in nums:
            if item%2==0:
                prefix.append(0)
            else:
                prefix.append(1)
                
        prefix_count=defaultdict(int)
        prefix_count[0]=1
        prefix_sum=0

        count=0
        
        for num in prefix:
            prefix_sum+=num
            count+=prefix_count.get(prefix_sum-k,0)
            prefix_count[prefix_sum]+=1
            
        return count