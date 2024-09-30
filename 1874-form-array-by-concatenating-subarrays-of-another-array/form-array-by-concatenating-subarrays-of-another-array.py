class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        n = len(nums)
        m = len(groups)

        idx = 0
        i=0

        #idx is index for nums
        #i is index for groups
        #j is index for groups[i]
        
        while idx<n:
            current_idx = idx #store idx before iteration
            j=0
            while j<len(groups[i]) and idx<n and nums[idx]==groups[i][j]:
                j+=1
                idx+=1
            
            if j==len(groups[i]):
                i+=1
            else:
                idx = current_idx+1
            #print(idx,i)
            if i>=m:
                return True
                
        return False