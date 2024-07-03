class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0 or indexDiff < 0:
            return False

        bucket_size = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):
            bucket_id = num // bucket_size

            if bucket_id in buckets:
                return True
            
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) < bucket_size:
                return True
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) < bucket_size:
                return True
            
            buckets[bucket_id] = num

            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // bucket_size]
        
        return False
        '''for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(j-i)>indexDiff:
                    break
                if abs(nums[j]-nums[i]) <= valueDiff:
                    return True
        return False'''