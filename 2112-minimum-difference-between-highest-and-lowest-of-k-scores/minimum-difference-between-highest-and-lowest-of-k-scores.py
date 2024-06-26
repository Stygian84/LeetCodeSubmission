class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        nums.sort()

        arr=deque([])
        min_score=math.inf
        for item in nums:
            arr.append(item)
            if len(arr)>k:
                arr.popleft()
            if len(arr)==k:
                diff=arr[-1]-arr[0]
                min_score=min(min_score,diff)

        return min_score
