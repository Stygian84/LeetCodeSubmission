class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_stack = deque() 
        min_stack = deque()  
        l = 0
        res = 0
        
        for r in range(len(nums)):
            
            while max_stack and nums[max_stack[-1]] <= nums[r]:
                max_stack.pop()
            max_stack.append(r)
            
            
            while min_stack and nums[min_stack[-1]] >= nums[r]:
                min_stack.pop()
            min_stack.append(r)
            
            
            while nums[max_stack[0]] - nums[min_stack[0]] > limit:
                l += 1
                if max_stack[0] < l:
                    max_stack.popleft()
                if min_stack[0] < l:
                    min_stack.popleft()
            
            
            res = max(res, r - l + 1)
        
        return res
            
        