class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        queue=deque(nums)

        res=-math.inf
        while queue:
            value=queue.pop()+queue.popleft()
            if value>res:
                res=value
        return res