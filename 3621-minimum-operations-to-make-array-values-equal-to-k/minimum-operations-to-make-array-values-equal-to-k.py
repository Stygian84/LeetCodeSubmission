class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        unique = set()
        inside = False
        for num in nums:
            if num<k:
                return -1
            unique.add(num)
            if num == k:
                inside = True

        if inside:
            return len(unique)-1
        return len(unique)