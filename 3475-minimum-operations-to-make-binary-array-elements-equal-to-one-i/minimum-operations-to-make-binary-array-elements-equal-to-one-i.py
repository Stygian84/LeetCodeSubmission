class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        q=deque()
        res=0
        k=3

        for i in range(n):
            if q and q[0]+k<=i:
                q.popleft()
            if len(q)%2==nums[i]:
                if i+k>n:
                    return -1
                q.append(i)
                res+=1        
        return res
        '''count=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                count+=1
                nums[i]=1
                nums[i+1]^=1
                nums[i+2]^=1
            else:
                continue
        if nums[-1]==0 or nums[-2]==0:
            return -1
        return count'''
