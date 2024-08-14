class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2

            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low
        
        '''distance = []
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                item1,item2 = nums[i],nums[j]

                heapq.heappush(distance, abs(item1-item2))

        res = 0
        for _ in range(k):
            res = heapq.heappop(distance)
        
        return res'''