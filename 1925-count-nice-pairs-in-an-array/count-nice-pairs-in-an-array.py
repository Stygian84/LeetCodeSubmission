class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0
        freq = defaultdict(int)

        def rev(x):
            num=str(x)[::-1]
            if num=="0":
                return 0
            num=num.lstrip('0')
            return int(num)


        for i in range(n):
            diff = nums[i]-rev(nums[i])

            if diff in freq:
                count+=freq[diff]
            freq[diff]+=1
        

        return (count) % (10**9+7)