class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # strictly increasing and then decreasing
        increasing = []
        front = []
        n = len(nums)
        for i in range(n):
            x = nums[i]
            pos = bisect_left(increasing, x)
            if pos == len(increasing):
                increasing.append(x)
            else:
                increasing[pos] = x
            front.append(len(increasing))

        nums = nums[::-1]
        decreasing = []
        back = []
        for i in range(n):
            x = nums[i]
            pos = bisect_left(decreasing, x)
            if pos == len(decreasing):
                decreasing.append(x)
            else:
                decreasing[pos] = x
            back.append(len(decreasing))
        back.reverse()

        max_mountain_length = 0
        for i in range(1, n - 1):
            if front[i] > 1 and back[i] > 1:
                max_mountain_length = max(max_mountain_length, front[i] + back[i] - 1)
       
        #print(increasing,decreasing)
        #print(front_idx,back_idx)    
        return n-max_mountain_length