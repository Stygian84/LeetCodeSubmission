class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        window = deque([])

        freq = defaultdict(int)
        total = 0
        res = 0
        for i in range(len(nums)):

            if len(window)==k:
               res = max(res,total)
        
            window.append(nums[i])
            freq[nums[i]]+=1
            total += nums[i]

            while freq[nums[i]]>1 or len(window)>k:
                removed = window.popleft()
                freq[removed]-=1
                total -= removed
                
    
        if len(window)==k:
            res = max(res,total)
            
        return res 
            
