class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=nums.count(1)
        if n == 0:
            return 0
        nums = nums*3
        res = math.inf


        k = 0
        count = 0
        window = deque()
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            window.append(nums[i])
            k+=1
            if k==n:
                if count<res:
                    res = count
                if window.popleft() == 0:
                    count-=1
                k-=1

        return res