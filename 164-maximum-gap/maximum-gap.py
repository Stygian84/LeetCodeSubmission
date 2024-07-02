class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def bucket_sort(arr):
            num_buckets = len(arr)
            max_value = max(arr)
            buckets = [[] for _ in range(num_buckets)]

            for x in arr:
                index = int(x * num_buckets / (max_value + 1))
                buckets[index].append(x)

            sorted_arr = []
            for bucket in buckets:
                sorted_arr.extend(sorted(bucket))
            
            return sorted_arr
        nums=bucket_sort(nums)
        if len(nums)<=1:
            return 0
        res=-math.inf

        for i in range(len(nums)-1):
            diff=nums[i+1]-nums[i]
            if diff>res:
                res=diff
        return res
        