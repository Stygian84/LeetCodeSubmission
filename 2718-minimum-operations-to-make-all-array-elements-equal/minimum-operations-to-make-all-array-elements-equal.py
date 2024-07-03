class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        prefix_sum = [0]*n
        prefix_sum[0] = nums[0]
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        def binSearch(target):
            l,r=0,n-1
            while l<=r:
                mid = (l+r) // 2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return l
        
        res = []
        for query in queries:
            pos = binSearch(query)

            sum_left = prefix_sum[pos-1]
            if pos == 0 :
                sum_left = 0
            
            sum_right = prefix_sum[-1] - sum_left

            operations = abs(query * (pos) - sum_left) + abs(query * (n - pos) - sum_right)
            res.append(operations)

        return res