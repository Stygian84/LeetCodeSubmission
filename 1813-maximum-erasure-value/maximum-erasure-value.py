class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ls=deque([])
        seen=set()
        total=0
        max_total=0

        for item in nums:
            while item in seen:
                num=ls.popleft()
                seen.remove(num)
                total-=num
            seen.add(item)
            ls.append(item)
            total+=item
            max_total=max(max_total,total)
        return max_total
    