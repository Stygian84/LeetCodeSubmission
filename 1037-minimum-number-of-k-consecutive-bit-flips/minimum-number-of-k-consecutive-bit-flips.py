class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        n=len(nums)
        q=deque()
        res=0

        for i in range(n):
            
            if q and q[0]+k<=i:
                q.popleft()
            if len(q)%2==nums[i]:
                if i+k>n:
                    return -1
                q.append(i)
                res+=1        
        return res
