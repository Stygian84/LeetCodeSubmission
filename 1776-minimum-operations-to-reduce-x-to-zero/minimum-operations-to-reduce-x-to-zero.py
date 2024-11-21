class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)

        #find longest subsequence whose total is sum(nums)-x
        res = math.inf

        window = deque([])
        target = sum(nums)-x
        total = 0
        print(target)
        for i in range(n):
            window.append(nums[i])
            total += nums[i]
    
            while window and total>target:
                total -= window.popleft()
            if total == target:
                res = min(res,n-len(window))
            

        if res == math.inf:
            return -1
        return res
