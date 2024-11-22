class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n%k!=0:
            return False
        nums.sort()
        freq = Counter(nums)
        count = 0
        for i in range(n):
            if freq[nums[i]]==0:
                continue
            for j in range(k):
                freq[nums[i]+j]-=1
                if freq[nums[i]+j]<0:
                    return False
            count+=1
        
        return True