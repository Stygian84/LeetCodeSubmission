class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        n = len(nums)
        marked = [False]*n

        temp = []
        for i in range(n):
            temp.append((nums[i],i))
        
        temp.sort(key = lambda x: (-x[0],-x[1]))
        
        score = 0
        while temp:
            num,idx = temp.pop()
            if marked[idx]==True:
                continue

            marked[idx]=True

            score+=num

            if idx<n-1:
                marked[idx+1]=True
            if idx>0:
                marked[idx-1]=True
            
        return score