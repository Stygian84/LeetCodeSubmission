class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        freq = defaultdict(int)

        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]!=nums[j]:
                    freq[nums[i]*nums[j]]+=1
        total = 0
        for v in freq.values():
            if v>=2:
                total+=v*(v-1)//2*8
        return total
