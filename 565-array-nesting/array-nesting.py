class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        maximum = 0
        visited = [False] * len(nums)
        
        for i in range(len(nums)):
            if not visited[i]:
                start = i
                count = 0
                while not visited[start]:
                    visited[start] = True
                    start = nums[start]
                    count += 1
                maximum = max(maximum, count)
                
        return maximum
        '''maximum = 1
        memo = {}
        def dfs(start,seen):
            nonlocal maximum,memo

            item = nums[start]

            if item not in seen and item not in memo:
                seen.add(item)
                dfs(item,seen)
            else:
                maximum = max(len(seen),maximum)
                memo[start]=maximum
                return

        for num in nums:
            dfs(num,set())
        
        return maximum'''