class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        res = []
        new = []
        for i in range(n):
            new.append( (nums[i], i) )
        
        new.sort()
        l,r = 0 , n-1
        while l<r:
            total = new[l][0]+new[r][0]
            if total==target:
                return [new[l][1],new[r][1]]
            elif total<target:
                l+=1
                while l<r and new[l][0]==new[l-1][0]:
                    l+=1
            else:
                r-=1
                while l<r and new[r][0]==new[r+1][0]:
                    r-=1

        '''ls = []
        for idx in range(0, len(nums)):
            new_num = target - nums[idx]
            if new_num in nums[idx + 1 :]:
                ls.append(idx)
                ls.append(nums[idx + 1 :].index(new_num) + idx + 1)
                return ls
            else:
                continue'''
