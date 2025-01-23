class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        unique = set()
        for num in nums:
            if num<k:
                return -1
            unique.add(num)

        if k in unique:
            return len(unique)-1
        return len(unique)