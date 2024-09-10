class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count=0
        n = len(nums)
        dc = defaultdict(int)

        for i in range(n):
            diff = nums[i]-i
            if diff in dc:
                count+=dc[diff]

            dc[diff]+=1
        

        return n*(n-1)//2-count