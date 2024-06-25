class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)

        max_count=0
        for num in nums:
            count=1
            temp=num+1
            while temp in s:
                s.remove(temp)
                count+=1
                temp+=1
            
            temp=num-1
            while temp in s:
                s.remove(temp)
                count+=1
                temp-=1
                
            if count>max_count:
                max_count=count
            
            count=0
        return max_count